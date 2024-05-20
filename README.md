# funasr-wrapper

### Install

```
cd funasr-wrapper

virtualenv -p python3 myenv
source myenv/bin/activate

git clone https://github.com/alibaba/FunASR.git && cd FunASR
pip3 install -e ./

pip3 install -U modelscope
```

### Test

测试加标点:

```
./main_restore_punct.sh ./example/input.json ./example/ouput.json
```

测试转录：

```
./main_transcribe.sh ./example/早咖啡.m4a ./example/out.json 生动早咖啡
```