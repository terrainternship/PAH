Скрипт и ноутбук для компиляции в EXE файл
Чтобы создать exe файл в Python, можно воспользоваться модулем PyInstaller. PyInstaller — это пакет, который позволяет создавать автономные исполняемые файлы (exe) для приложений Python, которые могут запускаться на компьютерах без установленного Python.

Для создания exe файла с помощью PyInstaller необходимо выполнить следующие шаги:

Установить PyInstaller с помощью pip:

pip install pyinstaller

Перейти в папку, содержащую ваш скрипт Python, и выполнить команду:

pyinstaller --onefile имя_скрипта.py

где имя_скрипта.py — это имя вашего скрипта.

PyInstaller создаст папку dist, в которой будет содержаться ваш exe файл.
Обратите внимание, что при создании exe файла могут возникать проблемы с зависимостями. Например, если ваш скрипт использует сторонние библиотеки, PyInstaller может не смочь правильно определить их зависимости. В этом случае необходимо явно указать зависимости с помощью параметров командной строки PyInstaller.

В Папку с EXE файлом нужно скопировать файл .CSV  и .h5 

Для удобства работы с консольным выводом делаем .cmd с именем нашего .exe файла c текстом:

VVP_predict2.exe >> Report.txt

После выполнения в директории появится Report.txt c содержанием :
![image](https://github.com/terrainternship/PAH/assets/126348122/5042b111-bcb1-46dc-91b5-d388fdd673b6)
Так же можно сохранить графики вручную через кнопки 
![image](https://github.com/terrainternship/PAH/assets/126348122/9684a5c8-5e01-4b71-8c95-7248edbb768c)


![image](https://github.com/terrainternship/PAH/assets/126348122/45ea9a2b-ed70-4c5b-9349-2656c49e999c)


![image](https://github.com/terrainternship/PAH/assets/126348122/27873d79-e442-48a1-847d-1fe2786fc837)
![image](https://github.com/terrainternship/PAH/assets/126348122/fbd8da2f-7473-4e9f-9834-c8612cbe6867)
![image](https://github.com/terrainternship/PAH/assets/126348122/d4abebbc-3687-4b4d-9de9-5e6805629271)
