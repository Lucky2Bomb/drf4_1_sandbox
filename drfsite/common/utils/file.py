import uuid
from datetime import datetime


def upload_to(self, filename, directory='images'):
    dt_path_str = datetime.strftime(datetime.now(), '%Y-%m')

    new_filename = '{name}.{extension}'.format(
        name=uuid.uuid4(), extension=filename.split('.')[-1])

    return '{directory}/{path}/{filename}'.format(
        directory=directory,
        path=dt_path_str,
        filename=new_filename
    )
