@echo off

echo please make sure that default Python version is 3.10.x

pip install requests

REM python download.py

python -m pip install --upgrade pip

echo composing venv
IF NOT EXIST venv (
    python -m venv venv
) ELSE (
    echo venv folder already exists, skipping making new venv...
)
call .\venv\Scripts\activate.bat


pip3 install torch==2.2.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 --upgrade
pip install https://github.com/jllllll/bitsandbytes-windows-webui/releases/download/wheels/bitsandbytes-0.41.2.post2-py3-none-win_amd64.whl --upgrade
pip install transformers --upgrade
pip install xformers==0.0.24 --upgrade
pip install sentencepiece
pip install opencv-python
pip install accelerate


echo installing triton 3
pip install https://huggingface.co/MonsterMMORPG/SECourses/resolve/main/triton-2.1.0-cp310-cp310-win_amd64.whl --upgrade


echo Installing required packages from requirements.txt...
pip install -r requirements.txt

echo installing requirements
pip install https://huggingface.co/MonsterMMORPG/SECourses/resolve/main/deepspeed-0.11.2_cuda121-cp310-cp310-win_amd64.whl --upgrade
pip install gradio

echo all install completed. please verify no errors
REM Exit the batch file
pause
