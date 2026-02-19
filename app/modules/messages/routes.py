# app/modules/messages/routes.py

from flask import render_template, request, flash, redirect, url_for
from . import messages_bp
from . import services

@messages_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 1. Ambil data dari Form HTML
        content = request.form.get('content')

        try:
            # 2. Lempar ke Service untuk diproses
            services.process_new_message(content)
            flash('Pesan berhasil dikirim!', 'success')
            return redirect(url_for('messages.index'))
        
        except ValueError as e:
            # Error validasi (kosong/kepanjangan)
            flash(str(e), 'error')
        except Exception as e:
            # Error database atau lainnya
            print(f"Error: {e}")
            flash('Terjadi kesalahan sistem.', 'error')

    # 3. Ambil daftar pesan untuk ditampilkan di bawah form
    messages_data = services.get_messages_list()

    return render_template('messages/index.html', messages=messages_data)