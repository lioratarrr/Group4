from flask import Blueprint, render_template, request, jsonify
from utilities.db.db_connector import save_inquiry

contactus = Blueprint(
    'contactus',
    __name__,
    static_folder='static',
    static_url_path='/contactus/static',
    template_folder='templates',
)

@contactus.route('/contactus')
def contact_us_func():
    return render_template('contactus.html')

@contactus.route('/save_inquiry', methods=['POST'])
def save_inquiry_func():
    data = request.get_json()
    # Extract fields from the received data
    fullname = data.get('fullname')
    phone = data.get('phone')
    info = data.get('info')

    inquirydata = {
        'fullname': fullname,
        'phone': phone,
        'info': info,
    }

    try:
        if save_inquiry(inquirydata):
            return jsonify({'status': 'success', 'message': 'Request saved successfully'})
        else:
            return jsonify({'status': 'error', 'message': 'Failed to save request'}), 500
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error saving request: {str(e)}'}), 500
