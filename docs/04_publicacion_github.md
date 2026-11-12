# Publicación en GitHub (cuenta `cesarlorcabacian`)

Destino: <https://github.com/cesarlorcabacian/mcdi502-s3-formativa3>

> Tu cuenta ya tiene `proyecto-grupo6-mcdi500` y `proyecto-grupo6-mcdi500-entrega-` (otro curso). Este repositorio es **nuevo**; no se mezcla con ellos.
> Si el grupo usa un nombre propio, puedes renombrarlo, p. ej. `mcdi502-s3-formativa3-grupoN`; en ese caso actualiza las URLs del `README.md` (badges y enlace de Colab).

## Opción 1 — GitHub CLI (`gh`)
```bash
unzip mcdi502-s3-formativa3.zip && cd mcdi502-s3-formativa3
gh auth login                                   # una sola vez
git init && git add . && git commit -m "Formativa 3 - MCDI502 S3"
git branch -M main
gh repo create cesarlorcabacian/mcdi502-s3-formativa3 --private --source=. --remote=origin --push
```
Cambia `--private` por `--public` si corresponde.

## Opción 2 — Web + git
1. Crea el repositorio vacío en <https://github.com/new> con nombre `mcdi502-s3-formativa3` (sin README, sin .gitignore, sin licencia).
2. Ejecuta:
```bash
unzip mcdi502-s3-formativa3.zip && cd mcdi502-s3-formativa3
git init && git add . && git commit -m "Formativa 3 - MCDI502 S3"
git branch -M main
git remote add origin https://github.com/cesarlorcabacian/mcdi502-s3-formativa3.git
git push -u origin main
```
(GitHub pedirá un Personal Access Token como contraseña, o usa SSH.)

## Trabajo en grupo
- Agrega a los compañeros en **Settings > Collaborators**, o pide que hagan *fork* y *pull request*.
- Cada integrante trabaja en una rama (`git checkout -b feature/<nombre>`) y propone cambios por PR.
- Los cambios en la configuración del notebook y la lógica de ingesta quedan validados por el workflow `validate`.

## Recomendaciones
- Mantenlo **privado** hasta que cierre la actividad y se publique el solucionario (integridad académica).
- No subas tokens ni URIs con credenciales.
- Tras publicar, verifica en la pestaña **Actions** que `validate` quede en verde.
