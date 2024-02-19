pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests

rm -rf NIX 

git clone --depth=1 https://github.com/Mr-Nix8/kazi.git

cd kazi

git pull

python nix.py

