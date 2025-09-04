
"""
Домашнее задание дом.задание_2
"""
"""
Задание 1
При решении заданий необходимо использовать репо-
зиторий на GitHub. Используйте ваш аккаунт на GitHub.
Если у вас его нет, создайте.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
аккаунт на GitHub создан
репозиторий - https://github.com/ev-g-hash/ev-g-hash.git

Задание 2
Создайте папку c набором подпапок и файлов.
создана папка \ev-g-hash
создана подпапки ev-g-hash\\1 и ev-g-hash\\2
файлы 1_1, 1_2, 2_1, 2_2 (один файл был переименован qqqf.txt -> 1/1_1.txt)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Задание 3
Создайте репозиторий в главной папке.
в папке \ev-g-hash создан репозиторий .git
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Задание 4
Добавьте всё содержимое папки в индекс репозитория
с помощью команды: git add.
добавлено
        $ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        renamed:    qqqf.txt -> 1/1_1.txt
        new file:   1/1_2.txt
        new file:   2/2_1.txt
        new file:   2/2_2.txt

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Задание 5
Создайте commit на основании данных, добавленных
в индекс. Используйте команду: git commit.
commit создан
                $ git commit -m "первый"
                [master 073650d] первый
                 4 files changed, 0 insertions(+), 0 deletions(-)
                 rename qqqf.txt => 1/1_1.txt (100%)
                 create mode 100644 1/1_2.txt
                 create mode 100644 2/2_1.txt
                 create mode 100644 2/2_2.txt


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Задание 6
Создайте новую ветку с названием newbranch.
создана новая ветка newbranch
                            прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (master)
                            $ git checkout -b newbranch
                            Switched to a new branch 'newbranch'
                            
                            прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (newbranch)
                            $

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Задание 7
Создайте новую подпапку с набором файлов, наполните их данными.
После наполнения создайте commit c содержимым новой подпапки в ветке newbranch.
создана подпапка 3 в ней два файла 3_1.txt, 3_2.txt
сделан commit
                прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (newbranch)
                $ git add .
                
                прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (newbranch)
                $ git status
                On branch newbranch
                Changes to be committed:
                  (use "git restore --staged <file>..." to unstage)
                        new file:   3/3_1.txt
                        new file:   3/3_2.txt                            
                               
                прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (newbranch)
                $ git commit -m "запись первая newbranch"
                [newbranch 034c792] запись первая newbranch
                 2 files changed, 0 insertions(+), 0 deletions(-)
                 create mode 100644 3/3_1.txt
                 create mode 100644 3/3_2.txt
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Задание 8
Перейдите в ветку master. Создайте новую подпапку
с файлами, наполните их данными. После наполнения
создайте commit c содержимым новой подпапки в ветке
master.
перешел в ветку мастер
                    прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (newbranch)
                    $ git checkout master
                    Switched to branch 'master'
                    
                    прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (master)
                    $
создана папка 4 в ней два файла 4_1.txt и 4_2.txt
создан commit
            прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (master)
            $ git add .
            
            прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (master)
            $ git commit -m "второй мастер"
            [master 75fbb3b] второй мастер
             2 files changed, 0 insertions(+), 0 deletions(-)
             create mode 100644 4/4_1.txt
             create mode 100644 4/4_2.txt
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Задание 9
Перейдите в ветку newbranch. Слейте содержимое
ветки master с веткой newbranch.
перешёл в ветку newbranch
                        прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (master)
                        $ git checkout newbranch
                        Switched to branch 'newbranch'
                        
                        прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (newbranch)
                        $
слил содержимое ветки master с веткой newbranch
                    прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (newbranch|MERGING)
                    $

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Задание 10
Перейдите в ветку master. Внесите изменения в не-
сколько существующих файлов. Изменения должны при-
вести к конфликтам при слиянии. Создайте commit с
изменениями.
перешёл в ветку мастер
                        прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (master)
                        $
внёс изменения в файлы 1_1.txt и 1_2.txt 
создан commit с изменениями
                        $ git commit -m "изменения слияния"
                        [master 158fa60] изменения слияния
                         2 files changed, 2 insertions(+)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Задание 11
Перейдите в ветку newbranch. Слейте содержимое
веткиmaster с веткой newbranch. Решите конфликты при
их возникновении.
конфликт разрешён 
                    прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (newbranch)
                    $ git checkout master
                    Switched to branch 'master'
                    
                    прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (master)
                    $ git status
                    On branch master
                    nothing to commit, working tree clean
                    
                    прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (master)
                    $ git checkout newbranch
                    Switched to branch 'newbranch'
                    
                    прога@DESKTOP-DVDB3QE MINGW64 ~/Desktop/ev-g-hash (newbranch)
                    $ git status
                    On branch newbranch
                    nothing to commit, working tree clean
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""