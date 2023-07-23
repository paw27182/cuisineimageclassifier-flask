# import ast
from datetime import datetime as dt
from pathlib import Path

from flask import Blueprint, render_template, request

import appmain.command as cmd

mid = Path(__file__).name  # module id
ftime = "%Y/%m/%d %H:%M:%S"

appmain_bp = Blueprint('appmain_bp', __name__,
                       template_folder='templates/appmain',
                       static_url_path='/appmain/static',
                       static_folder='../appmain/static',
                       )


@appmain_bp.route("/appmain", methods=["POST"])
def appmain():
    command = request.form.get("command")
    # command = ast.literal_eval(list(request.form.values())[0]).get('command')  # request form Spring Boot3

    msg = f'{dt.now().strftime(ftime)} [{mid}] --- @appmain_bp.route("/appmain") --- command: {command} ---'
    print(msg)

    if command in ["submit_an_image"]:
        file = request.files["data_file"]
        file_name = file.filename

        if file_name[-4:] not in [".jpg", ".png"] and file_name[-5:] not in [".jpeg"]:
            return render_template('area4Submit.html',
                                   message="NG. Unsupported file type",
                                   alert="NG")

        input_data = file.stream.read()
        answer, images = cmd.predict_image(input_data)

        return render_template('area4Result.html',
                               message=f"The answer is {answer}.",
                               images=images,
                               alert="OK")
    else:
        pass
