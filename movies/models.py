# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from django.db.models import F

class CountryArea(models.Model):
    country_area_id = models.AutoField(primary_key=True)
    country_area_name = models.CharField(unique=True, max_length=100)
    m49_code = models.SmallIntegerField()
    iso_alpha3_code = models.CharField(max_length=3)
    dev_status = models.ForeignKey('DevStatus', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country_area'
        ordering = ['country_area_name']
        verbose_name = 'UNSD M49 Country or Area'
        verbose_name_plural = 'UNSD M49 Countries or Areas'

    def __str__(self):
        return self.country_area_name
    def get_absolute_url(self):
        return reverse('country_detail', args=[str(self.pk)])		


'''
class CountryArea(models.Model):
    country_area_id = models.AutoField(primary_key=True)
    country_area_name = models.CharField(unique=True, max_length=100)
    region = models.ForeignKey('Region', models.DO_NOTHING, blank=True, null=True)
    sub_region = models.ForeignKey('SubRegion', models.DO_NOTHING, blank=True, null=True)
    intermediate_region = models.ForeignKey('IntermediateRegion', models.DO_NOTHING, blank=True, null=True)
    m49_code = models.SmallIntegerField()
    iso_alpha3_code = models.CharField(max_length=3)
    dev_status = models.ForeignKey('DevStatus', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country_area'
'''


class DevStatus(models.Model):
    dev_status_id = models.AutoField(primary_key=True)
    dev_status_name = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'dev_status'
        ordering = ['dev_status_name']
        verbose_name = 'UNSD M49 Country or Area Development Status'
        verbose_name_plural = 'UNSD M49 Country or Area Development Statuses'

    def __str__(self):
        return self.dev_status_name


'''
class DevStatus(models.Model):
    dev_status_id = models.AutoField(primary_key=True)
    dev_status_name = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'dev_status'
'''


'''
class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'color'
'''
class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'color'
        ordering = ['color_name']
        verbose_name = 'Movie Color'
        verbose_name_plural = 'Movie Colors'    

    def __str__(self):
        return self.color_name        

'''
class ContentRating(models.Model):
    content_rating_id = models.AutoField(primary_key=True)
    content_rating = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'content_rating'
'''
class ContentRating(models.Model):
    content_rating_id = models.AutoField(primary_key=True)
    content_rating = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'content_rating'
        ordering = ['content_rating']
        verbose_name = 'Movie ContentRating'
        verbose_name_plural = 'Movie ContentRatings'    

    def __str__(self):
        return self.content_rating
        

        
'''
class Director(models.Model):
    director_id = models.AutoField(primary_key=True)
    director_name = models.CharField(unique=True, max_length=225)

    class Meta:
        managed = False
        db_table = 'director'
'''
class Director(models.Model):
    director_id = models.AutoField(primary_key=True)
    director_name = models.CharField(unique=True, max_length=225)

    class Meta:
        managed = False
        db_table = 'director'
        ordering = ['director_name']
        verbose_name = 'Movie director_name'
        verbose_name_plural = 'Movie director_names'    

    def __str__(self):
        return self.director_name        

'''
class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'genre'
'''
class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'genre'
        ordering = ['genre']
        verbose_name = 'Movie genre'
        verbose_name_plural = 'Movie genres'    

    def __str__(self):
        return self.genre        
 
'''
class PlotKeyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keyword = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'plot_keyword'
'''
class PlotKeyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keyword = models.CharField(unique=True, max_length=225)

    class Meta:
        managed = False
        db_table = 'plot_keyword'
        ordering = ['keyword']
        verbose_name = 'Movie keyword'
        verbose_name_plural = 'Movie keywords'

    def __str__(self):
        return self.keyword 

'''
class MovieLanguage(models.Model):
    language_id = models.AutoField(primary_key=True)
    language_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'movie_language'
'''
class MovieLanguage(models.Model):
    language_id = models.AutoField(primary_key=True)
    language_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'movie_language'
        ordering = ['language_name']
        verbose_name = 'Language Name'
        verbose_name_plural = 'Language Names'

    def __str__(self):
        return self.language_name
		

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_title = models.CharField(unique=True, max_length=225)
    title_year = models.IntegerField()  # This field type is a guess.
    imdb_score = models.DecimalField(max_digits=2, decimal_places=1)
    duration = models.IntegerField()
    movie_imdb_link = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    director = models.ForeignKey(Director, on_delete=models.PROTECT)
    language = models.ForeignKey(MovieLanguage, on_delete=models.PROTECT)
    country_area = models.ForeignKey(CountryArea, on_delete=models.PROTECT)
    content_rating = models.ForeignKey(ContentRating, on_delete=models.PROTECT)
    
    genre = models.ManyToManyField(Genre, through='MovieGenres')
    keyword = models.ManyToManyField(PlotKeyword, through='MovieKeywords')
	
    class Meta:
        managed = False
        db_table = 'movie'
        ordering = ['movie_title']
        verbose_name = 'movie'
        verbose_name_plural = 'movies'    

    def __str__(self):
        return self.movie_title
    def genre_display(self):
        """Create a string for country_area. This is required to display in the Admin view."""
        return ', '.join(
            genre.genre for genre in self.genre.all()[:25])

    genre_display.short_description = 'genres'        

    def get_absolute_url(self):
        return reverse('singlemovie', args=[str(self.pk)])

    @property
    def movie_genres(self):
        genres = self.genre.order_by('genre')

        names = []
        for genre in genres:
            name = genre.genre
            if name is None:
                continue

            genrename = ''.join([name])
            if genrename not in names:
                names.append(genrename)

        return ', '.join(names)
    @property
    def movie_keywords(self):
        keywords = self.keyword.order_by('keyword')
        #print(keywords)
        names = []
        for keyword in keywords:
            name = keyword.keyword
            if name is None:
                continue

            keywordname = ''.join([name])
            #print(keywordname)			
            if keywordname not in names:
                names.append(keywordname)
        print(', '.join(names))
        return ', '.join(names)
		
		
'''
class MovieGenres(models.Model):
    movie_genres_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, models.DO_NOTHING)
    genre = models.ForeignKey(Genre, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movie_genres'
'''
class MovieGenres(models.Model):
    movie_genres_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'movie_genres'
        ordering = ['movie', 'genre']
        verbose_name = 'MovieGenre'
        verbose_name_plural = 'MovieGenres'

        
'''
class MovieKeywords(models.Model):
    movie_keywords_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, models.DO_NOTHING)
    keyword = models.ForeignKey('PlotKeyword', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movie_keywords'
'''
class MovieKeywords(models.Model):
    movie_keywords_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    keyword = models.ForeignKey(PlotKeyword, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'movie_keywords'
        ordering = ['movie', 'keyword']
        verbose_name = 'MovieKeyword'
        verbose_name_plural = 'MovieKeywords'        

        

        
       