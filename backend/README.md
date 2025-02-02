# django-ninja
基于django 的后端项目。

## 主要技术栈
* django
* django-ninja
* seldom

## 安装

* 安装依赖

```shell
> pip install -r requirements.txt
```

* 执行数据库同步

```
> python manage.py makemigrations
> python manage.py migrate
```
* Redis
  - Windows: https://github.com/tporadowski/redis
  - Linux：https://github.com/redis/redis

```shell
> redis-server  # 启动redis
```

## 运行

* 开发运行

```shell
> python manage.py runserver
```

* 部署运行

```shell
> uwsgi --ini uwsgi.ini
```

> 部署事项：
> 1. uwsgi 推荐在Linux上安装
> 2. 修改`uwsgi.ini` 中项目路径，带 `->` 配置项需要修改
> 3. 关闭 `backend/setting.py` 文件中设置 `debug=False`

## 查看接口

* 浏览器访问：http://localhost:8000/api/docs

![](./api.png)

