@echo off
ngrok.exe -config ngrok.cfg -subdomain=feynman 8000
echo ������ngrok http://feynman.tunnel.phpor.me ===> 0.0.0.0:8000
