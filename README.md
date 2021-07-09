# istio-examples

## Framework
<img src="https://raw.githubusercontent.com/AniChikage/istio-examples/main/assets/book-info.png" width = "500" height = "300" alt="" align=center />

## Introduction

Service:
+ front-page: simple book info front page, calling details service
+ details: two versions
  + v1: just calling ratings service
  + v2: calling ratings and comments service
+ ratings: two versions
  + v1: just "rating" field
  + v2: adding "people_number" field
+ comments: new feature in details-v2, user's comments for book

## Setup

### Install and config Istio

1. download istio

```
curl -L https://istio.io/downloadIstio | sh -
cd istio-1.10.2
mv bin/istioctl /usr/bin/
```

2. install instio for openshift

use openshift configuration files, then istio is installed into a namespace "istio-system"
```
istioctl install --set profile=openshift -y
```

3. create a namespace for your project
```
oc new-project <your namespace>
```

4. add anyuid to the namespace
```
oc adm policy add-scc-to-group anyuid system:serviceaccounts:<your namespace>
```

```
cat <<EOF | oc -n <your namespace> create -f -
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: istio-cni
EOF
```

5. inject istio into the namespace
```
oc label namespace <your namespace> istio-injection=enabled
```

6. check if istio is correctly installed in namespace
```
istioctl analyze
```

7. open kiali dashboard
```
istioctl dashboard kiali
```

### Deploy Book-info application

1. go to platform folder, apply all yamls by order

```
cd /platform
oc apply -f 00_book-ratings-v1.yaml
oc apply -f 01_book-ratings-v2.yaml
oc apply -f 02_book-details-v1.yaml
oc apply -f 03_book_comments-v1.yaml
oc apply -f 04_book-details-v2.yaml
oc apply -f 05_book-front-page-v1.yaml
```

2. expose services

you can view service by `oc get svc`
```
comments     ClusterIP   172.30.154.90    <none>        5000/TCP   2d1h
details      ClusterIP   172.30.245.185   <none>        5000/TCP   2d1h
front-page   ClusterIP   172.30.53.193    <none>        5000/TCP   2d1h
ratings      ClusterIP   172.30.29.85     <none>        5000/TCP   2d1h
```

expose them
```
oc expose svc ratings
oc expose svc details
oc expose svc comments
oc expose svc front-page
```

then you can get routes by `oc get routes`
```
comments     comments-book-info.apps.ocp-xo3xv-xx8ue.ibmdtepaks.com            comments     http                 None
details      details-book-info.apps.ocp-xo3xv-xx8ue.ibmdtepaks.com             details      http                 None
front-page   front-page-book-info.apps.ocp-xo3xv-xx8ue.ibmdtepaks.com          front-page   http                 None
ratings      ratings-book-info.apps.ocp-xo3xv-xx8ue.ibmdtepaks.com             ratings      http                 None
```

you can access them by url in brownser such as: comments-book-info.apps.ocp-xo3xv-xx8ue.ibmdtepaks.com


### Istio traffic experiments

1. go to networking folder, apply destination rules, this tells istio to route traffic to target service and its version

```
cd ./networking
oc apply -f 20-destination-rule-details.yaml
oc apply -f 21-destination-rule-ratings.yaml
```

2. apply 01 and 04

```
oc apply -f 01-virtual-service-ratings-v1.yaml
oc apply -f 04-virtual-service-details-v1.yaml
```

refresh `front-page-book-info.apps.ocp-xo3xv-xx8ue.ibmdtepaks.com`, only show ratings, no comments. This means calling details-v1 and ratings-v1

3. apply the rest yamls as you like, see what happened

