"""Exercicios 3:"""

'''3. Crie as classes Televisao com atributo status, volume, canal e ControleRemoto com o atributo televisao, de forma que:
    a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
    b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
    c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também permitir que
    seja informado um número de canal para efetuar a troca;'''

class Televisao:

    def __init__(self):
        self.__status: bool = False
        self.__volume: int = 0
        self.__canal: int = 0

    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, status: bool) -> None:
        self.__status = status

    @property
    def volume(self)-> int:
        return self.__volume

    @volume.setter
    def volume(self, volume: int)-> None:
        self.__volume = volume




