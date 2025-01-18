from flask import Blueprint, render_template

category = Blueprint(
  'category',
  __name__,
  static_folder='static',
  static_url_path='/category/static',
  template_folder='templates',
)

from flask import Flask, render_template

app = Flask(__name__)

categories_data = {
'homepage': {
    'title': 'דף הבית',
    'category': [
    {'name': 'עגילי רוני', 'image': 'jewelery/Earings/ronigold.png', 'alt': 'עגילי רוני זהב', 'description': '', 'product_images': ['jewelery/Earings/ronigold.png', 'jewelery/Earings/ronisilver.png']},
    {'name': 'טבעת לולה', 'image': 'jewelery/Rings/lolagold.png', 'alt': 'טבעת לולה זהב', 'description': '', 'product_images': ['jewelery/Rings/lolagold.png', 'jewelery/Rings/lolasilver.png']},
    {'name': 'שרשרת אות', 'image': 'jewelery/Necklaces/lettergold.png', 'alt': 'שרשרת אות זהב', 'description': '', 'product_images': ['jewelery/Necklaces/lettergold.png', 'jewelery/Necklaces/lettersilver.png']},
    {'name': 'שרשרת ארץ ישראל', 'image': 'jewelery/Sale/israelneck.png', 'alt': 'שרשרת ארץ ישראל', 'description': '', 'product_images': ['jewelery/Sale/israelneck.png']},
    {'name': 'עגילי סבינה', 'image': 'jewelery/Earings/sabinagold.png', 'alt': 'עגילי סבינה זהב', 'description': '', 'product_images': ['jewelery/Earings/sabinagold.png', 'jewelery/Earings/sabinasilver.png']}
    ]
  },
  'bracelets': {
    'title': 'צמידים',
    'category': [
      {'name': 'צמיד דנה', 'image': 'jewelery/Bracelets/danagold.png', 'alt': 'צמיד דנה',
       'description': 'צמיד עם עיצוב חוליות גדולות'},
      {'name': 'צמיד לב', 'image': 'jewelery/Bracelets/heartgold.png', 'alt': 'צמיד לב זהב',
       'description': 'צמיד עם תליון לב מעוצב בעדינות'},
      {'name': 'צמיד מגן דוד', 'image': 'jewelery/Bracelets/davidgold.png', 'alt': 'צמיד מגן דוד זהב',
       'description': 'צמיד עם תליון מגן דוד, עדין ואלגנטי  מתאים לאירועים עם משמעות יהודית או יום-יום',
       'image_silver': 'jewelery/Bracelets/davidsilver.png'},
      {'name': 'צמיד שיבולים', 'image': 'jewelery/Bracelets/oatgold.png', 'alt': 'צמיד שיבולים זהב',
       'description': 'צמיד בהשראת שיבולים, עיצוב טבעי ופשוט  מושלם למראה קלאסי ונקי',
       'image_silver': 'jewelery/Bracelets/oatsilver.png'},
      {'name': 'צמיד שם', 'image': 'jewelery/Bracelets/namegold.png', 'alt': 'צמיד שם זהב',
       'description': 'צמיד עם תליון בהתאמה אישית לשם, מתנה ייחודית עם נגיעה אישית',
       'image_silver': 'jewelery/Bracelets/namesilver.png'}
    ]
  },
  'earings': {
    'title': 'עגילים',
    'category': [
      {'name': 'עגילי גסיקה', 'image': 'jewelery/Earings/jesicagold.png', 'alt': 'עגילי גסיקה',
       'description': 'עגילים עם פנינה בעיצוב קלאסי ועדין, מושלמים להוספת טאץ׳ יוקרתי לכל הופעה',
       'image_silver': 'jewelery/Earings/jesicasilver.png'},
      {'name': 'עגילי ליאור', 'image': 'jewelery/Earings/liorgold.png', 'alt': 'עגילי ליאור זהב',
       'description': 'עגילים בצורת פרח, עדינים וקלילים, מתאימים למראה טבעי וצעיר',
       'image_silver': 'jewelery/Earings/liorsilver.png'},
      {'name': 'עגילי סבינה', 'image': 'jewelery/Earings/sabinagold.png', 'alt': 'עגילי סבינה זהב',
       'description': 'עגילים עם תליון לב, רומנטיים ונשיים, משלימים הופעה למראה ייחודי',
       'image_silver': 'jewelery/Earings/sabinasilver.png'},
      {'name': 'עגילי סמבה', 'image': 'jewelery/Earings/sambagold.png', 'alt': 'עגילי סמבה זהב',
       'description': 'עגילים בעלי עיצוב חלק ומבריק, מתאימים למראה אלגנטי או יום-יומי',
       'image_silver': 'jewelery/Earings/sambasilver.png'},
      {'name': 'עגילי רוני', 'image': 'jewelery/Earings/ronigold.png', 'alt': 'עגילי רוני זהב',
       'description': 'עגילים בצורת לב, עיצוב קלאסי ונצחי, מושלמים למראה רומנטי ומיוחד',
       'image_silver': 'jewelery/Earings/ronisilver.png'}
    ]
  },
  'necklaces': {
    'title': 'שרשראות',
    'category': [
      {'name': 'שרשרת אוריין', 'image': 'jewelery/Necklaces/oriannegold.png', 'alt': 'שרשרת אוריין זהב',
       'description': 'שרשרת עדינה עם תליון לב, מתאימה למראה קלאסי ורומנטי',
       'image_silver': 'jewelery/Necklaces/oriannesilver.png'},
      {'name': 'שרשרת אות', 'image': 'jewelery/Necklaces/lettergold.png', 'alt': 'שרשרת אות זהב',
       'description': 'שרשרת אלגנטית עם תליון מותאם אישית, מושלמת למתנה עם נגיעה אישית',
       'image_silver': 'jewelery/Necklaces/lettersilver.png'},
      {'name': 'שרשרת יסמין', 'image': 'jewelery/Necklaces/yasmingold.png', 'alt': 'שרשרת יסמין זהב',
       'description': 'שרשרת יוקרתית עם חרוזים קטנים, מעוצבת למראה ייחודי ונשי',
       'image_silver': 'jewelery/Necklaces/yasminsilver.png'},
      {'name': 'שרשרת רעות', 'image': 'jewelery/Necklaces/reutgold.png', 'alt': 'שרשרת רעות זהב',
       'description': 'שרשרת שכבות עם תליון עדין, מתאימה לאירועים מיוחדים ולמראה אלגנטי',
       'image_silver': 'jewelery/Necklaces/reutsilver.png'},
      {'name': 'שרשרת שחף', 'image': 'jewelery/Necklaces/shahafgold.png', 'alt': 'שרשרת שחף זהב',
       'description': 'שרשרת בעלת עיצוב חלק ופשוט, מושלמת למראה יום-יומי או קלאסי',
       'image_silver': 'jewelery/Necklaces/shahafsilver.png'}
    ]
  },
  'rings': {
    'title': 'טבעות',
    'category': [
      {'name': 'טבעת אמילי', 'image': 'jewelery/Rings/emiligold.png', 'alt': 'טבעת אמילי זהב',
       'description': 'טבעת עם עיצוב מודרני וגיאומטרי, מושלמת להשלמת מראה ייחודי',
       'image_silver': 'jewelery/Rings/emilisilver.png'},
      {'name': 'טבעת לולה', 'image': 'jewelery/Rings/lolagold.png', 'alt': 'טבעת לולה זהב',
       'description': 'טבעת בעיצוב חוליות אלגנטי, מתאימה למראה יומיומי וקלאסי',
       'image_silver': 'jewelery/Rings/lolasilver.png'},
      {'name': 'טבעת מישל', 'image': 'jewelery/Rings/mishelgold.png', 'alt': 'טבעת מישל זהב',
       'description': 'טבעת משובצת באבנים עדינות, מעניקה טאץ׳ יוקרתי ונשי',
       'image_silver': 'jewelery/Rings/mishelsilver.png'},
      {'name': 'טבעת פרפר', 'image': 'jewelery/Rings/butterflygold.png', 'alt': 'טבעת פרפר זהב',
       'description': 'טבעת עם עיצוב פרפרים עדין, מושלמת להוספת אלמנט טבעי וייחודי',
       'image_silver': 'jewelery/Rings/butterflysilver.png'},
      {'name': 'טבעת קלואי', 'image': 'jewelery/Rings/chloegold.png', 'alt': 'טבעת קלואי זהב',
       'description': 'טבעת בעלת טקסטורה מעוגלת, מתאימה לכל אירוע ולמראה קלאסי',
       'image_silver': 'jewelery/Rings/chloesilver.png'}
    ]
  },
  'sale': {
    'title': 'הנחות',
    'category': [
      {'name': 'שרשרת רוסנה', 'image': 'jewelery/Sale/rosananeck.png', 'alt': 'שרשרת רוסנה',
       'description': 'שרשרת עם חוליות זהב אלגנטיות, מתאימה למראה יומיומי או ערב', 'image_silver': ''},
      {'name': 'סט עגילים רבקה', 'image': 'jewelery/Sale/rivkaset.png', 'alt': 'סט עגילים רבקה',
       'description': 'סט עגילים הכולל עיצובים מגוונים, מושלם להשלמת כל לוק', 'image_silver': ''},
      {'name': 'עגילי דניאלה', 'image': 'jewelery/Sale/danielaearings.png', 'alt': 'עגילי דניאלה',
       'description': 'עגילים מעוצבים עם מוטיב פרחוני, מתאימים למראה עדין וטבעי', 'image_silver': ''},
      {'name': 'עגילי ליאנה', 'image': 'jewelery/Sale/lianaearings.png', 'alt': 'עגילי ליאנה',
       'description': 'עגילים עגולים עם פנינה עדינה, משלימים מראה יוקרתי ונשי', 'image_silver': ''},
      {'name': 'שרשרת ארץ ישראל', 'image': 'jewelery/Sale/israelneck.png', 'alt': 'שרשרת ארץ ישראל',
       'description': 'שרשרת כסופה עם תליון בצורת מפת ישראל, מסמלת זהות וגאווה', 'image_silver': ''}
    ]
  }
}

@category.route('/category/<category_name>')
def category_func(category_name):
    # Check if the category exists in categories_data
    category_data = categories_data.get(category_name)
    if category_data:
        return render_template('category.html', category_title=category_data['title'], products=category_data['category'])
    else:
        return "Category not found", 404
@category.route('/')
def homepage_func():
  category_data = categories_data.get('homepage')
  return render_template('category.html', category_title=category_data['title'], products=category_data['category'])

