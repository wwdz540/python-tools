# python-tools
## me.json.tool 
‘ 用于打印格式化json,及根据字符串路径查找路由

``` shell
echo '[{"name":"王志平","dept":"开发部"},{"name":"王","dept":"开发部"}]' | python -m me.json.tool --path 1.name
```

```shell
 cat <<EOF | python -m me.json.tool --path roles.1.name
 {
  "name":"王志平",
  "roles":[
      {"id":11,"name":"超级管理员"},
      {"id":12,"name":"运维"},
      {"id":12,"name":"系统管理员"}
  ]
 }
EOF
```
