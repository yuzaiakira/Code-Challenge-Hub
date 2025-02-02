from datetime import datetime


def generate_file_name(instance, filename):
    username = instance.user.username
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    
    return f'{username}/{timestamp}-{filename}'
