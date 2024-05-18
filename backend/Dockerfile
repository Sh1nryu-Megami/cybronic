FROM php:8.2-apache

ENV APACHE_DOCUMENT_ROOT /var/www/html/public/

RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf
ENV COMPOSER_ALLOW_SUPERUSER=1

RUN a2enmod rewrite

WORKDIR /var/www/html/
COPY . .
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer
RUN composer install

