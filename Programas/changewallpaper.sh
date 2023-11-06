#!/bin/bash

# Rutas y variables de configuración
inifile="/home/emmanuel/changewallpaper.ini"
schema="org.cinnamon.desktop.background"
key="picture-uri"
options="picture-options"
folder="/home/emmanuel/Pictures/Papel tapiz"

PID=$(pgrep -fo cinnamon-session)

export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ | tr -d '\0' | cut -d= -f2-)


# Leer el número de archivo actual desde el archivo de configuración
if [[ -f "$inifile" ]]; then
  file_number=$(awk -F= '/filenumber/ {print $2}' "$inifile")
fi

# Obtener la lista de archivos de la carpeta de fondo de pantalla
files=("$folder"/*)
num_files=${#files[@]}

# Asegurarse de que el número de archivo no sea mayor que el número de archivos disponibles
  ((file_number++))
if ((file_number >= num_files)); then
  file_number=0
fi

# Cambiar la configuración del fondo de pantalla
gsettings set "$schema" "$key" "file://${files[file_number]}"
gsettings set "$schema" "$options" "scaled"

# Notificar el cambio de fondo de pantalla
notify-send "ChangeWallpaper" "${files[file_number]}"

# Actualizar el número de archivo seleccionado en el archivo de configuración
sed -i "s/filenumber=.*/filenumber=$file_number/" "$inifile"
