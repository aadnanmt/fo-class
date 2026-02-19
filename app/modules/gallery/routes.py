# app/modules/gallery/routes.py

from flask import render_template, request, flash, redirect, url_for
from . import gallery_bp
from . import services

@gallery_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # ceck post request
        if 'photo' not in request.files:
            flash('Tidak ada file yang dipilih', 'error')
            return redirect(request.url)
        
        file = request.files['photo']
        
        try:
            # send file to service.py
            services.process_upload(file)
            flash('foto berhasil diupload', 'success')
            return redirect(url_for('gallery.index'))

        # error handling
        except ValueError as e:
            flash(str(e), 'error')
        except Exception as e:
            print(f"upload error: {e}")
            flash('gagal upload. cek koneksi atau ukuran filemu.', 'error')

    # select all n photos supabase
    photos = services.get_photos()
    
    return render_template('gallery/index.html', photos=photos)