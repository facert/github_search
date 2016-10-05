# github_search

### 介绍
根据 keywords 搜索 github 上面的 repos, 并通过 web 展示

### 安装
  * 安装 redis 
  
   > apt-get install redis-server
      
  * 安装依赖
  
  > pip install requirements.txt
  
### run
  * run 搜索结果的脚本
  
  > python github_search.py 

  * 开启 web 服务, 访问 http://127.0.0.1:5000/
  
  > python app.py
  
### 搜索参数配置
  * github_search.py 里面 修改 keywords = ['', '', ''] 可以定制搜索
  
### screenshots

  ![demo](https://raw.githubusercontent.com/facert/github_search/master/screenshots/demo.png)
  
