# istio-systems

## Framework
<img src="https://raw.githubusercontent.com/AniChikage/istio-examples/main/assets/book-info.png" width = "500" height = "300" alt="" align=center />

## Introduction

Service:
+ front-page: simple book info front page, calling details service
+ details: two versions
  + v1: just calling ratings service
  + v2: calling ratings and comments service
+ ratings: two versions
  + v1: just "rating"
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

3. deploy app to your own namespace

```
oc adm policy add-scc-to-group anyuid system:serviceaccounts:book-info
```

