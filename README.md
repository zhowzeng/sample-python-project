# Sample Python Project

此專案

* 不依賴 poetry/pdm
* 沒有要作為 package 供其他專案使用。
* 打包成 image 執行

## Docker

```bash
# build
docker build -t <image-tag> --build-arg "GID=$(id -g)" --build-arg "UID=$(id -u)" .
# run command
docker run -it -u $(id -g):$(id -u) <image-tag> <command>
# run bash for debugging
docker run -it -u $(id -g):$(id -u) --entrypoint bash <image-tag> <command>
```
