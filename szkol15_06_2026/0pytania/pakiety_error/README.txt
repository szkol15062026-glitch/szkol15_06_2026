W folderach opis pakietów i modułów z przykładem co robić w sytuacji, gdy wywala nam błąd z brakiem modułu


# pakiety_error/
# +-- dao/
#    +-- __init__.py
#    +-- dao.py              
#    +-- poddao/
#        +-- __init__.py
#        +-- poddao.py         
#        +-- podpoddao/
#            +-- __init__.py       
#           +-- podpoddao.py 
# +-- testy/    
#     +-- __init__.py
#     +-- dao_test.py          # Problem z importem dao.py do dao_test.py



Dodatkowo linki rozwijające temat:

https://docs.python.org/3/tutorial/modules.html           --> Oficjalna dokumentacja --> moduły z pakietami
https://docs.python.org/3/reference/import.html           --> Oficjalna dokumentacja --> python i rozwiązywanie importów
https://docs.python.org/3/library/sys.html#sys.path       --> Oficjalna dokumentacja --> sys.path 
https://docs.python.org/3/using/cmdline.html#cmdoption-m  --> Oficjalna dokumentacja --> uruchamiania modułu jako skryptu

Pep-y:

https://peps.python.org/pep-0008/#imports     --> styl importów
https://peps.python.org/pep-0328/             --> importy względne
https://peps.python.org/pep-0420/             --> folder bez __init__


Real python:
https://realpython.com/python-modules-packages/ 


inne:
https://gaopinghuang0.github.io/2018/08/03/python3-import-and-project-layout