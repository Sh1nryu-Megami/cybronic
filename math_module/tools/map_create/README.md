# map_create.py - SVG to JSON

Это утилита для вытягивания информации о пространстве из `.svg` файла
и последующего преобразования в `.json`.

Просто напишите `python map_create.py -f svg/_file_.svg`, где `_file_`
название файла, который вы хотите преобразовать, чтобы получить разметку
помещения.

* Напишите `python map_create.py -h` и увидете посказку по использованию:

> `someuser:~$ python map_create.py -h`<br/>
> This program transform svg file with halls and lighthouses
> to *.json file which contains coordinates of the halls and
> lighthouses.<br/>
> 
> Commands:<br/>
>   -h - gets this message;<br/>
>   -f - svg file;<br/>
>   -o - place where do you want to place the output file,<br/>
> if -o doesn't exist the output will be placed in the ./output directory,<br/>
> if you don't pass path that ends with a filename then a filename will be<br/>
> equal to the input filename without the extension;<br/>
> <br/>
> Name of output file is name of input with .json extention.<br/>