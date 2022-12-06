# 利用ガイド
### 起動方法
1. intern-edu-2022ディレクトリで `docker-compose up -d`
2. intern-edu-2022ディレクトリで `docker-compose exec app bash`
3. `tmux`を入力しtmuxを起動
4. Ctrl+b 後 % で画面を縦に分割 (Tips: Ctrl+b 後 → or ← で分割画面を移動できる)
5. `cd frontend` 後 `npm install`
6. `npm run dev`　でフロントエンドを起動
7. 別画面で `cd backend` 後 `python server.py` でバックエンドを起動

### 前提
- DockerDesktopインストール (https://www.docker.com/products/docker-desktop/)
- Githubへの登録 (https://github.com/)
- SourceTreeインストール (https://www.sourcetreeapp.com/)
