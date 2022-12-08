# 利用ガイド
### 起動方法
1. intern-edu-2022ディレクトリで `docker-compose up -d`
2. intern-edu-2022ディレクトリで `docker-compose exec app bash` windows `winpty` を頭につける
3. 別のウィンドウから2.を実行
4. `cd frontend` 後 `npm install`
5. `npm run dev`　でフロントエンドを起動
6. 別画面で `cd backend` 後 `python server.py` でバックエンドを起動
7. ブラウザで `localhost` にアクセス

### 前提
- DockerDesktopインストール (https://www.docker.com/products/docker-desktop/)
- Githubへの登録 (https://github.com/)
- SourceTreeインストール (https://www.sourcetreeapp.com/)
