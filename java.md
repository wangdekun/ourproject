```
thymeleaf是java服务端的模板引擎,能够处理HTML,XML,JAVASCRIPT和文本,主要目标是提供自然地,,高度可维护性的模板.基于自然模板的概念,将逻辑注入模板文件中,切不影响其设计原型.
```
#2018.8.11wdk
```
在创建springboot时,第一次运行SpringBootApplication若遇见--"'url' attribute is not specified and no embedded datasource could be configured."错误--,则,在@SpringBootApplication注解后加(exclude = {DataSourceAutoConfiguration.class}),更改后即为@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
```
#2018.8.13
```
在第一次配置springboot时,如果pom.xml文件已经写了mysql包,可是application.properties文件的mysql.jdbc报红,鼠标放上去提示cannot resovle class or package....,这时候可以去project structure里的library里引入mysql包,这时候就不会报错了
```

#2018.8.14
```
@RestController是@Controller和@ResponseBody的结合体,@ResponseBody 加载Controller表明整个的Controller中都是返回数据而不是去找相应的页面地址！！！！
```

```
springboot默认访问ftl页面,因此若要设置访问HTML页面需要给application.properties配置文件添加spring.freemarker.suffix=.html即可
```