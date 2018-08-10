# Accio
## What's accio?
Accio is a simple way to open projects and files from the command line in you favorite editor. With Accio you can assign nick names to files, so once they're added there's no need to type out (or remember) full filepaths. Perfect for those pesky config files hidden in the heart of your system!

## Setting your editor
```
accio editor <path>

accio editor code #sets the default editor to vs code
```

## Assigning nicknames to files

```
accio add <nickname> <filepath>

accio add hosts /etc/hosts
accio add apache-vhosts /etc/apache2/sites-available/000-default.conf
accio add php.ini /etc/php/7.2/apache2/php.ini
accio add my-project /www/my/project/folder
```
## Listing files added to accio

```
accio ls

    hosts           /etc/hosts
    apache-vhosts   /etc/apache2/sites-available/000-default.conf
    php.ini         /etc/php/7.2/apache2/php.ini
    my-project      /www/my/project/folder
```

You can also filter the list by filename making things super easy to find:
```
accio ls php

    php.ini         /etc/php/7.2/apache2/php.ini
```

## Removing files added to accio
```
accio rm <nickname>

accio rm php.ini
```

## Opening a file or folder
```
accio run php.ini   #opens php.ini in your editor
accio run myproject #opens the folder in your editor
```