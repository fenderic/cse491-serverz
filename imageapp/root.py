import quixote
from quixote.directory import Directory, export, subdir
from quixote.util import StaticFile
import os.path

from . import html, image

class RootDirectory(Directory):
    _q_exports = []

    @export(name='')                    # this makes it public.
    def index(self):
        return html.render('index.html')
        
        
    @export(name='jquery.js')
    def jquery(self):
        return html.render('jquery-1.11.0.min.js')
        
    @export(name='ajaxUpload.js')
    def ajax_upload(self):
        return html.render('ajaxUpload.js')
        
        
    @export(name='upload')
    def upload(self):
        return html.render('upload.html')

        
    @export(name='upload_receive')
    def upload_receive(self):
        request = quixote.get_request()
        print request.form.keys()

        the_file = request.form['file']
        name = request.form['image_name']
        desc = request.form['image_desc']

        print dir(the_file)
        print 'received file with name: ', the_file.base_filename
        print 'image name: ', name
        print 'image desc: ', desc

        data = the_file.read(the_file.get_size())

        image.add_image(the_file.base_filename, data, name, desc)

        return quixote.redirect('./')


    @export(name='upload2')
    def upload2(self):
        return html.render('upload2.html')

        
    @export(name='upload2_receive')
    def upload2_receive(self):
        request = quixote.get_request()
        print request.form.keys()

        the_file = request.form['file']
        name = request.form['image_name']
        desc = request.form['image_desc']
        
        print dir(the_file)
        print 'received file with name:', the_file.base_filename
        data = the_file.read(the_file.get_size())

        image.add_image(the_file.base_filename, data, name, desc)

        return html.render('upload2_received.html')
        
        
    @export(name='image')
    def image(self):
        #return html.render('image.html')
        return html.render('image.html', {'image_name' : image.get_latest_image()[1], 'image_desc' : image.get_latest_image()[2]})


        
    @export(name='image_raw')
    def image_raw(self):
        response = quixote.get_response()
        response.set_content_type('image/png')
        img = image.get_latest_image()
        #img = image.get_latest_image()[0]
        return img        
        
    @export(name='image_raw2')
    def image_raw2(self):
        response = quixote.get_response()
        response.set_content_type('image/png')
        img = image.get_first_image()
        return img
        
        
    @export(name='guestbook_view')
    def guestbook(self):
        return html.render('guestbook_view.html')
        
    @export(name='guestbook_write')
    def guestbook_write(self):
        return html.render('guestbook_write.html')
        
    @export(name='guestbook_add')
    def guestbook_add(self):
#        return html.render('guestbook_add.html')
        return html.render('http://www.google.com')
