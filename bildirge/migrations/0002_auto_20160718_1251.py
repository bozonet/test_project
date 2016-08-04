# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bildirge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinsiyet', models.CharField(choices=[('M', 'Erkek'), ('F', 'Bayan')], default='SOME STRING', max_length=1)),
                ('unvan', models.CharField(choices=[('P', 'Prof. Dr.'), ('D', 'Doc. Dr.'), ('Y', 'Yard. Doc. Dr.'), ('U', 'Uzm. Dr.'), ('Dr', 'Dr.'), ('B', 'Biyolog'), ('O', 'Ogr. Gor.'), ('A', 'Aras. Gor.'), ('T', 'Teknisyen'), ('M', 'Muhendis'), ('D.O.', 'Doktora Ogrencisi'), ('Mr', 'Bay'), ('Ms', 'Bayan')], default='SOME STRING', max_length=2)),
                ('isim', models.CharField(default='Burasi doldurulmalidir', max_length=120)),
                ('soyad', models.CharField(default='Burasi doldurulmalidir', max_length=120)),
                ('kurum', models.CharField(default='Burasi doldurulmalidir', max_length=120)),
                ('bolum', models.CharField(default='Burasi doldurulmalidir', max_length=120)),
                ('gorev', models.CharField(blank=True, max_length=120, null=True)),
                ('uzmanlik', models.CharField(blank=True, max_length=120, null=True)),
                ('adres', models.CharField(default='Burasi doldurulmalidir', max_length=120)),
                ('posta_kodu', models.CharField(blank=True, max_length=120, null=True)),
                ('sehir', models.CharField(default='Burasi doldurulmalidir', max_length=120)),
                ('ulke', models.CharField(choices=[('AD', 'Andorra'), ('AE', 'United Arab Emirates'), ('AF', 'Afghanistan'), ('AG', 'Antigua & Barbuda'), ('AI', 'Anguilla'), ('AL', 'Albania'), ('AM', 'Armenia'), ('AN', 'Netherlands Antilles'), ('AO', 'Angola'), ('AQ', 'Antarctica'), ('AR', 'Argentina'), ('AS', 'American Samoa'), ('AT', 'Austria'), ('AU', 'Australia'), ('AW', 'Aruba'), ('AZ', 'Azerbaijan'), ('BA', 'Bosnia and Herzegovina'), ('BB', 'Barbados'), ('BD', 'Bangladesh'), ('BE', 'Belgium'), ('BF', 'Burkina Faso'), ('BG', 'Bulgaria'), ('BH', 'Bahrain'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BN', 'Brunei Darussalam'), ('BO', 'Bolivia'), ('BR', 'Brazil'), ('BS', 'Bahama'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'), ('CF', 'Central African Republic'), ('CG', 'Congo'), ('CH', 'Switzerland'), ('CI', 'Ivory Coast'), ('CK', 'Cook Iislands'), ('CL', 'Chile'), ('CM', 'Cameroon'), ('CN', 'China'), ('CO', 'Colombia'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CV', 'Cape Verde'), ('CX', 'Christmas Island'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DE', 'Germany'), ('DJ', 'Djibouti'), ('DK', 'Denmark'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('DZ', 'Algeria'), ('EC', 'Ecuador'), ('EE', 'Estonia'), ('EG', 'Egypt'), ('EH', 'Western Sahara'), ('ER', 'Eritrea'), ('ES', 'Spain'), ('ET', 'Ethiopia'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands (Malvinas)'), ('FM', 'Micronesia'), ('FO', 'Faroe Islands'), ('FR', 'France'), ('FX', 'France, Metropolitan'), ('GA', 'Gabon'), ('GB', 'United Kingdom (Great Britain)'), ('GD', 'Grenada'), ('GE', 'Georgia'), ('GF', 'French Guiana'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GL', 'Greenland'), ('GM', 'Gambia'), ('GN', 'Guinea'), ('GP', 'Guadeloupe'), ('GQ', 'Equatorial Guinea'), ('GR', 'Greece'), ('GS', 'South Georgia and the South Sandwich Islands'), ('GT', 'Guatemala'), ('GU', 'Guam'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('HM', 'Heard & McDonald Islands'), ('HN', 'Honduras'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('ID', 'Indonesia'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IQ', 'Iraq'), ('IR', 'Islamic Republic of Iran'), ('IS', 'Iceland'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KE', 'Kenya'), ('KG', 'Kyrgyzstan'), ('KH', 'Cambodia'), ('KI', 'Kiribati'), ('KM', 'Comoros'), ('KN', 'St. Kitts and Nevis'), ('KP', "Korea, Democratic People's Republic of"), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('KY', 'Cayman Islands'), ('KZ', 'Kazakhstan'), ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanon'), ('LC', 'Saint Lucia'), ('LI', 'Liechtenstein'), ('LK', 'Sri Lanka'), ('LR', 'Liberia'), ('LS', 'Lesotho'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('LY', 'Libyan Arab Jamahiriya'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('MD', 'Moldova, Republic of'), ('MG', 'Madagascar'), ('MH', 'Marshall Islands'), ('ML', 'Mali'), ('MN', 'Mongolia'), ('MM', 'Myanmar'), ('MO', 'Macau'), ('MP', 'Northern Mariana Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MS', 'Monserrat'), ('MT', 'Malta'), ('MU', 'Mauritius'), ('MV', 'Maldives'), ('MW', 'Malawi'), ('MX', 'Mexico'), ('MY', 'Malaysia'), ('MZ', 'Mozambique'), ('NA', 'Namibia'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NI', 'Nicaragua'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NU', 'Niue'), ('NZ', 'New Zealand'), ('OM', 'Oman'), ('PA', 'Panama'), ('PE', 'Peru'), ('PF', 'French Polynesia'), ('PG', 'Papua New Guinea'), ('PH', 'Philippines'), ('PK', 'Pakistan'), ('PL', 'Poland'), ('PM', 'St. Pierre & Miquelon'), ('PN', 'Pitcairn'), ('PR', 'Puerto Rico'), ('PT', 'Portugal'), ('PW', 'Palau'), ('PY', 'Paraguay'), ('QA', 'Qatar'), ('RE', 'Reunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('SA', 'Saudi Arabia'), ('SB', 'Solomon Islands'), ('SC', 'Seychelles'), ('SD', 'Sudan'), ('SE', 'Sweden'), ('SG', 'Singapore'), ('SH', 'St. Helena'), ('SI', 'Slovenia'), ('SJ', 'Svalbard & Jan Mayen Islands'), ('SK', 'Slovakia'), ('SL', 'Sierra Leone'), ('SM', 'San Marino'), ('SN', 'Senegal'), ('SO', 'Somalia'), ('SR', 'Suriname'), ('ST', 'Sao Tome & Principe'), ('SV', 'El Salvador'), ('SY', 'Syrian Arab Republic'), ('SZ', 'Swaziland'), ('TC', 'Turks & Caicos Islands'), ('TD', 'Chad'), ('TF', 'French Southern Territories'), ('TG', 'Togo'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TM', 'Turkmenistan'), ('TN', 'Tunisia'), ('TO', 'Tonga'), ('TP', 'East Timor'), ('TR', 'Turkey'), ('TT', 'Trinidad & Tobago'), ('TV', 'Tuvalu'), ('TW', 'Taiwan, Province of China'), ('TZ', 'Tanzania, United Republic of'), ('UA', 'Ukraine'), ('UG', 'Uganda'), ('UM', 'United States Minor Outlying Islands'), ('US', 'United States of America'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VA', 'Vatican City State (Holy See)'), ('VC', 'St. Vincent & the Grenadines'), ('VE', 'Venezuela'), ('VG', 'British Virgin Islands'), ('VI', 'United States Virgin Islands'), ('VN', 'Viet Nam'), ('VU', 'Vanuatu'), ('WF', 'Wallis & Futuna Islands'), ('WS', 'Samoa'), ('YE', 'Yemen'), ('YT', 'Mayotte'), ('YU', 'Yugoslavia'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZR', 'Zaire'), ('ZW', 'Zimbabwe'), ('ZZ', 'Unknown or unspecified country')], default='Burasi doldurulmalidir', max_length=2)),
                ('is_tel', models.CharField(blank=True, max_length=120, null=True)),
                ('ev_tel', models.CharField(blank=True, max_length=120, null=True)),
                ('fax_no', models.CharField(blank=True, max_length=120, null=True)),
                ('cep_tel', models.CharField(default='Burasi doldurulmalidir', max_length=120)),
                ('email', models.EmailField(default='Burasi doldurulmalidir', max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('sifre', models.CharField(default='Burasi doldurulmalidir', max_length=120)),
                ('sifre_onay', models.CharField(default='Burasi doldurulmalidir', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='profile/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(default='Burasi doldurulmalidir', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='yazar',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
