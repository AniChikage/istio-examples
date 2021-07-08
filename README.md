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

1. download istio

```
curl -L https://istio.io/downloadIstio | sh -
cd istio-1.10.2
mv bin/istioctl /usr/bin/
```

2. install instio

use openshift configuration files
```
istioctl install --set profile=openshift -y
```

add namespace label
```
oc label namespace book-info istio-injection=enabled
```

3. new project
```
oc new-project book-info
```

4. deploy app to your own namespace
```
oc adm policy add-scc-to-group anyuid system:serviceaccounts:book-info
```

```
cat <<EOF | oc -n book-info create -f -
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: istio-cni
EOF
```

5. istio label namespace
```
oc label namespace book-info istio-injection=enabled
```

6. check if istio is correctly in namespace
```
istioctl analyze
```

check if istio yaml is right
```
istioctl validate -f <yaml file name>
``` 

7. open kiali dashboard
```
istioctl dashboard kiali
```