@echo off
TITLE Kanishka Management Bot
:: Enables virtual env mode and then starts Kanishka
env\scripts\activate.bat && py -m KanishkaBot
