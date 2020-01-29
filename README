# StarlightBot
[![GPLv3 license](https://img.shields.io/badge/Version-1.0-blueviolet.svg)](http://perso.crans.org/besson/LICENSE.html) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-lightgrey.svg)](https://www.python.org/) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

Starlight es un bot diseñado para proveer diversas utilidades en los grupos de Messenger. Está escrito en python3, y es software libre.

## Módulos
| Módulo | Descripción |
| :------------- | :------------- |
| animeflv | Devuelve los primeros 5 resultados del sitio web AnimeFLV. |
| ayuda | Muestra la ayuda de un comando. |
| bot | Informa sobre el bot. |
| calc | Realiza operaciones matemáticas. |
| corr | Realiza correcciones de mensajes. |
| dado | Lanza un dado y te dice el número que cayó. |
| google | Devuelve los primeros 8 resultados de búsqueda. |
| insulta | Pues eso, insulta. |
| insulto | Reconoce insultos comunes al bot, y actúa en consecuencia.  |
| lmgtfy | Para los flojos, un enlace a Google. |
| menciones | Si se envía el mensaje @todos, menciona a todos los integrantes. |
| mercadolibre | Devuelve los primeros 5 resultados del sitio web MercadoLibre. |
| moneda | Lanza una moneda y te dice si cayó sol o águila. |
| nhentai | Devuelve los primeros 5 resultados del sitio web nhentai.net. |
| nickbot | Vigila los cambios de nicknames, la foto, y el nombre del grupo. También los configura automáticamente por día. |
| ping | Si el bot está disponible, devuelve "pong". |
| tiempo | Muestra el estado del tiempo, y otros datos. Por ahora, sólo en Villahermosa. |
| wolfram | Consultas a Wolfram&#124;Alpha. Devuelve una imagen con el resultado. Útil para resolver ecuaciones, integrales, derivadas y graficar. |
| wp | Muestra un resumen de Wikipedia. Si no encuentra el artículo, muestra 5 posibles coincidencias para elegir a mostrar. |

## Dependencias
Starlight requiere el módulo ``fbchat`` para conectarse a Facebook. Puede instalarse simplemente haciendo:
```bash
$~ pip3 install fbchat
```
Otros módulos del bot requieren dependencias adicionales:
### lxml
Se requiere para los módulos ``animeflv``, ``mercadolibre`` y ``nhentai``. Instalación:
```bash
$~ apt-get install libxml1.1
$~ pip3 install lxml cssselect
```
### requests
Se requiere para los módulos ``animeflv``, ``mercadolibre``, ``nhentai``, ``tiempo`` y ``wp``. Instalación:
```bash
$~ pip3 install requests
```

## Uso <small style="font-style:italic;color:gray">(expandir)</small>
* Simplemente ejecute ``./starlight``
* La configuración se encuentra en el archivo ``config.json``. Dicho JSON tiene un objeto, donde cada propiedad corresponde a un módulo. La propiedad ``starlight`` está reservada para la configuración del propio bot.
* Es muy recomendable que el bot tenga permisos de escritura en la ruta donde se ejecute, para que le sea posible guardar la cookie de sesión.
