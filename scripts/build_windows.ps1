cd ..
# cleanup old build
rm -r dist
# use virtual environment
src/venv/Scripts/activate.ps1
# get pyinstaller
pip install pyinstaller
# create spec file
pyinstaller --clean -ywF -i src/icon.ico -n collisions src/main.py
# build exe
pyinstaller -y collisions.spec
# windows setup
mkdir dist/collisions
mv dist/collisions.exe dist/collisions/collisions.exe
# copy in assets
cp -r src/assets dist/collisions/assets
# copy in license
cp LICENSE.txt dist/collisions/
# copy in readme
cp README.txt dist/collisions/
# cleanup
deactivate
rm -r build
rm collisions.spec
cd scripts
