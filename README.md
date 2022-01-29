
# Botnet HTTP Template

Una plantilla básica para crear tu propia botnet, no solo el estilo del panel, sino que también a nivel funcional, ya que más adelante se podrá agregar módulos personalizados. Se irá completando poco a poco.

## Funcionamiento

![](https://i0.wp.com/securityaffairs.co/wordpress/wp-content/uploads/2013/04/04.jpg)

## Servidor C&C

### Instalar dependencias

```bash
pip3 install -r requirements.txt
```

### Configurar 

Editamos el archivo *config.py*:

```bash
vim config.py
```

### Ejecutar el C&C

```bash
python3 runserver.py
```

## Cliente 

### Ejecución

```bash
python3 client-v2.py
```

## Una muestra de este software

![](https://i.imgur.com/yCfx1lG.png)

## Advertencia

El mal uso de este software puede generar problemas legales y éticos de los cuales no apoyo y mucho menos me haré responsable.
