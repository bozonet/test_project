from __future__ import unicode_literals
from django.db import models
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
# http://xml.coverpages.org/country3166.html
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length =120, blank =False, null =False,default='Burasi doldurulmalidir')
    timestamp = models.DateTimeField(auto_now_add =True, auto_now=False)
    updated = models.DateTimeField(auto_now_add =False, auto_now=True)

    def __unicode__(self):
        return self.email

class Doc(models.Model):
    events = (
        (None, "Lutfen seciniz"),
        ('gtz', 'Genclik zirvesi'),
        ('tr', 'transist'),
    )
    Dosya = models.FileField(upload_to='uploads/')
    user = models.ForeignKey(User, null=True, blank=True)
    Etkinlik = models.CharField(max_length=15, choices=events, default='tr')

    def __unicode__(self):
        return unicode(self.user)



class MyUserManager(BaseUserManager):
    def create_user(self, email,   password=None ):
        
        
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),

            #date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return render(request, "form.html", context)
    
    def create_superuser(self, username,  password):
        
        
        
        u = self.create_user(username,
                        password=password,
                    )
        u.is_admin = True
        u.save(using=self._db)
        return render(request, "form.html", context)

class MyUser(AbstractBaseUser):
    
    username = models.CharField(max_length =120, blank =False, null =False,default='Burasi doldurulmalidir')
    email = models.EmailField(
                        verbose_name='email address',
                        max_length=255,
                        unique=True,
                    )


    #date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return render(request, "form.html", context)

def uploadImageView(request):
    if request.method == 'POST':
        form = File_form(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
    else:
        form = File_form()

    return render(request, 'uploadImagePage.html', {'uploadImageForm': form})

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Contact(models.Model):
    GENDER_CHOICES = (
        (None, "Lutfen seciniz"),
        ('M', 'Erkek'),
        ('F', 'Bayan'),
    )
    UNVAN_CHOICES = (
        (None, "Lutfen seciniz"),
        ('P', 'Prof. Dr.'),
        ('D', 'Doc. Dr.'),
        ('Y', 'Yard. Doc. Dr.'),
        ('U', 'Uzm. Dr.'),
        ('Dr', 'Dr.'),
        ('B', 'Biyolog'),
        ('O', 'Ogr. Gor.'),
        ('A', 'Aras. Gor.'),
        ('T', 'Teknisyen'),
        ('M', 'Muhendis'),
        ('D.O.', 'Doktora Ogrencisi'),
        ('Mr', 'Bay'),
        ('Ms', 'Bayan'),

    )

    COUNTRIES = (
    (None, "Lutfen seciniz"),
    ('AD', _('Andorra')),
    ('AE', _('United Arab Emirates')),
    ('AF', _('Afghanistan')),
    ('AG', _('Antigua & Barbuda')),
    ('AI', _('Anguilla')),
    ('AL', _('Albania')),
    ('AM', _('Armenia')),
    ('AN', _('Netherlands Antilles')),
    ('AO', _('Angola')),
    ('AQ', _('Antarctica')),
    ('AR', _('Argentina')),
    ('AS', _('American Samoa')),
    ('AT', _('Austria')),
    ('AU', _('Australia')),
    ('AW', _('Aruba')),
    ('AZ', _('Azerbaijan')),
    ('BA', _('Bosnia and Herzegovina')),
    ('BB', _('Barbados')),
    ('BD', _('Bangladesh')),
    ('BE', _('Belgium')),
    ('BF', _('Burkina Faso')),
    ('BG', _('Bulgaria')),
    ('BH', _('Bahrain')),
    ('BI', _('Burundi')),
    ('BJ', _('Benin')),
    ('BM', _('Bermuda')),
    ('BN', _('Brunei Darussalam')),
    ('BO', _('Bolivia')),
    ('BR', _('Brazil')),
    ('BS', _('Bahama')),
    ('BT', _('Bhutan')),
    ('BV', _('Bouvet Island')),
    ('BW', _('Botswana')),
    ('BY', _('Belarus')),
    ('BZ', _('Belize')),
    ('CA', _('Canada')),
    ('CC', _('Cocos (Keeling) Islands')),
    ('CF', _('Central African Republic')),
    ('CG', _('Congo')),
    ('CH', _('Switzerland')),
    ('CI', _('Ivory Coast')),
    ('CK', _('Cook Iislands')),
    ('CL', _('Chile')),
    ('CM', _('Cameroon')),
    ('CN', _('China')),
    ('CO', _('Colombia')),
    ('CR', _('Costa Rica')),
    ('CU', _('Cuba')),
    ('CV', _('Cape Verde')),
    ('CX', _('Christmas Island')),
    ('CY', _('Cyprus')),
    ('CZ', _('Czech Republic')),
    ('DE', _('Germany')),
    ('DJ', _('Djibouti')),
    ('DK', _('Denmark')),
    ('DM', _('Dominica')),
    ('DO', _('Dominican Republic')),
    ('DZ', _('Algeria')),
    ('EC', _('Ecuador')),
    ('EE', _('Estonia')),
    ('EG', _('Egypt')),
    ('EH', _('Western Sahara')),
    ('ER', _('Eritrea')),
    ('ES', _('Spain')),
    ('ET', _('Ethiopia')),
    ('FI', _('Finland')),
    ('FJ', _('Fiji')),
    ('FK', _('Falkland Islands (Malvinas)')),
    ('FM', _('Micronesia')),
    ('FO', _('Faroe Islands')),
    ('FR', _('France')),
    ('FX', _('France, Metropolitan')),
    ('GA', _('Gabon')),
    ('GB', _('United Kingdom (Great Britain)')),
    ('GD', _('Grenada')),
    ('GE', _('Georgia')),
    ('GF', _('French Guiana')),
    ('GH', _('Ghana')),
    ('GI', _('Gibraltar')),
    ('GL', _('Greenland')),
    ('GM', _('Gambia')),
    ('GN', _('Guinea')),
    ('GP', _('Guadeloupe')),
    ('GQ', _('Equatorial Guinea')),
    ('GR', _('Greece')),
    ('GS', _('South Georgia and the South Sandwich Islands')),
    ('GT', _('Guatemala')),
    ('GU', _('Guam')),
    ('GW', _('Guinea-Bissau')),
    ('GY', _('Guyana')),
    ('HK', _('Hong Kong')),
    ('HM', _('Heard & McDonald Islands')),
    ('HN', _('Honduras')),
    ('HR', _('Croatia')),
    ('HT', _('Haiti')),
    ('HU', _('Hungary')),
    ('ID', _('Indonesia')),
    ('IE', _('Ireland')),
    ('IL', _('Israel')),
    ('IN', _('India')),
    ('IO', _('British Indian Ocean Territory')),
    ('IQ', _('Iraq')),
    ('IR', _('Islamic Republic of Iran')),
    ('IS', _('Iceland')),
    ('IT', _('Italy')),
    ('JM', _('Jamaica')),
    ('JO', _('Jordan')),
    ('JP', _('Japan')),
    ('KE', _('Kenya')),
    ('KG', _('Kyrgyzstan')),
    ('KH', _('Cambodia')),
    ('KI', _('Kiribati')),
    ('KM', _('Comoros')),
    ('KN', _('St. Kitts and Nevis')),
    ('KP', _('Korea, Democratic People\'s Republic of')),
    ('KR', _('Korea, Republic of')),
    ('KW', _('Kuwait')),
    ('KY', _('Cayman Islands')),
    ('KZ', _('Kazakhstan')),
    ('LA', _('Lao People\'s Democratic Republic')),
    ('LB', _('Lebanon')),
    ('LC', _('Saint Lucia')),
    ('LI', _('Liechtenstein')),
    ('LK', _('Sri Lanka')),
    ('LR', _('Liberia')),
    ('LS', _('Lesotho')),
    ('LT', _('Lithuania')),
    ('LU', _('Luxembourg')),
    ('LV', _('Latvia')),
    ('LY', _('Libyan Arab Jamahiriya')),
    ('MA', _('Morocco')),
    ('MC', _('Monaco')),
    ('MD', _('Moldova, Republic of')),
    ('MG', _('Madagascar')),
    ('MH', _('Marshall Islands')),
    ('ML', _('Mali')),
    ('MN', _('Mongolia')),
    ('MM', _('Myanmar')),
    ('MO', _('Macau')),
    ('MP', _('Northern Mariana Islands')),
    ('MQ', _('Martinique')),
    ('MR', _('Mauritania')),
    ('MS', _('Monserrat')),
    ('MT', _('Malta')),
    ('MU', _('Mauritius')),
    ('MV', _('Maldives')),
    ('MW', _('Malawi')),
    ('MX', _('Mexico')),
    ('MY', _('Malaysia')),
    ('MZ', _('Mozambique')),
    ('NA', _('Namibia')),
    ('NC', _('New Caledonia')),
    ('NE', _('Niger')),
    ('NF', _('Norfolk Island')),
    ('NG', _('Nigeria')),
    ('NI', _('Nicaragua')),
    ('NL', _('Netherlands')),
    ('NO', _('Norway')),
    ('NP', _('Nepal')),
    ('NR', _('Nauru')),
    ('NU', _('Niue')),
    ('NZ', _('New Zealand')),
    ('OM', _('Oman')),
    ('PA', _('Panama')),
    ('PE', _('Peru')),
    ('PF', _('French Polynesia')),
    ('PG', _('Papua New Guinea')),
    ('PH', _('Philippines')),
    ('PK', _('Pakistan')),
    ('PL', _('Poland')),
    ('PM', _('St. Pierre & Miquelon')),
    ('PN', _('Pitcairn')),
    ('PR', _('Puerto Rico')),
    ('PT', _('Portugal')),
    ('PW', _('Palau')),
    ('PY', _('Paraguay')),
    ('QA', _('Qatar')),
    ('RE', _('Reunion')),
    ('RO', _('Romania')),
    ('RU', _('Russian Federation')),
    ('RW', _('Rwanda')),
    ('SA', _('Saudi Arabia')),
    ('SB', _('Solomon Islands')),
    ('SC', _('Seychelles')),
    ('SD', _('Sudan')),
    ('SE', _('Sweden')),
    ('SG', _('Singapore')),
    ('SH', _('St. Helena')),
    ('SI', _('Slovenia')),
    ('SJ', _('Svalbard & Jan Mayen Islands')),
    ('SK', _('Slovakia')),
    ('SL', _('Sierra Leone')),
    ('SM', _('San Marino')),
    ('SN', _('Senegal')),
    ('SO', _('Somalia')),
    ('SR', _('Suriname')),
    ('ST', _('Sao Tome & Principe')),
    ('SV', _('El Salvador')),
    ('SY', _('Syrian Arab Republic')),
    ('SZ', _('Swaziland')),
    ('TC', _('Turks & Caicos Islands')),
    ('TD', _('Chad')),
    ('TF', _('French Southern Territories')),
    ('TG', _('Togo')),
    ('TH', _('Thailand')),
    ('TJ', _('Tajikistan')),
    ('TK', _('Tokelau')),
    ('TM', _('Turkmenistan')),
    ('TN', _('Tunisia')),
    ('TO', _('Tonga')),
    ('TP', _('East Timor')),
    ('TR', _('Turkey')),
    ('TT', _('Trinidad & Tobago')),
    ('TV', _('Tuvalu')),
    ('TW', _('Taiwan, Province of China')),
    ('TZ', _('Tanzania, United Republic of')),
    ('UA', _('Ukraine')),
    ('UG', _('Uganda')),
    ('UM', _('United States Minor Outlying Islands')),
    ('US', _('United States of America')),
    ('UY', _('Uruguay')),
    ('UZ', _('Uzbekistan')),
    ('VA', _('Vatican City State (Holy See)')),
    ('VC', _('St. Vincent & the Grenadines')),
    ('VE', _('Venezuela')),
    ('VG', _('British Virgin Islands')),
    ('VI', _('United States Virgin Islands')),
    ('VN', _('Viet Nam')),
    ('VU', _('Vanuatu')),
    ('WF', _('Wallis & Futuna Islands')),
    ('WS', _('Samoa')),
    ('YE', _('Yemen')),
    ('YT', _('Mayotte')),
    ('YU', _('Yugoslavia')),
    ('ZA', _('South Africa')),
    ('ZM', _('Zambia')),
    ('ZR', _('Zaire')),
    ('ZW', _('Zimbabwe')),
    ('ZZ', _('Unknown or unspecified country')),
)
    user = models.ForeignKey(User,null=True)
    unvan = models.CharField(max_length=15, choices=UNVAN_CHOICES, default=None,error_messages={'required': 'Bu alan doldurulmalidir'})
    isim = models.CharField(max_length =120, blank =False, null =True,error_messages={'required': 'Bu alan doldurulmalidir'})
    soyad = models.CharField(max_length =120, blank =False, null =True,default='Burasi doldurulmalidir',error_messages={'required': 'Bu alan doldurulmalidir'})
    kurum = models.CharField(max_length =120, blank =False, null =False,default='Burasi doldurulmalidir',error_messages={'required': 'Bu alan doldurulmalidir'})
    bolum = models.CharField(max_length =120, blank =False, null =False,default='Burasi doldurulmalidir',error_messages={'required': 'Bu alan doldurulmalidir'})
    gorev = models.CharField(max_length =120, blank =True, null =True,error_messages={'required': 'Bu alan doldurulmalidir'})
    uzmanlik = models.CharField(max_length =120, blank =True, null =True,error_messages={'required': 'Bu alan doldurulmalidir'})
    adres = models.CharField(max_length =120, blank =False, null =False,default='Burasi doldurulmalidir',error_messages={'required': 'Bu alan doldurulmalidir'})
    posta_kodu = models.CharField(max_length =120, blank =True, null =True,error_messages={'required': 'Bu alan doldurulmalidir'})
    sehir= models.CharField(max_length =120, blank =False, null =False,default='Burasi doldurulmalidir',error_messages={'required': 'Bu alan doldurulmalidir'})
    ulke = models.CharField(max_length=2, choices=COUNTRIES, default='Burasi doldurulmalidir',error_messages={'required': 'Bu alan doldurulmalidir'})
    is_tel = models.CharField(max_length =120, blank =True, null =True,error_messages={'required': 'Bu alan doldurulmalidir'})
    ev_tel = models.IntegerField( blank =False, null =False,default='Burasi doldurulmalidir',error_messages={'required': 'Bu alan doldurulmalidir'})
    fax_no = models.IntegerField( blank =False, null =False,default='Burasi doldurulmalidir',error_messages={'required': 'Bu alan doldurulmalidir'})
    cep_tel = models.IntegerField( blank =False, null =False,default='Burasi doldurulmalidir',error_messages={'required': 'Bu alan doldurulmalidir'})
    timestamp = models.DateTimeField(auto_now_add =True, auto_now=False,error_messages={'required': 'Bu alan doldurulmalidir'})
    updated = models.DateTimeField(auto_now_add =False, auto_now=True,error_messages={'required': 'Bu alan doldurulmalidir'})
    #password2 = models.CharField(max_length =120, blank =False, null =False,default='Burasi doldurulmalidir')



    def __unicode__(self):
        return unicode(self.user)

