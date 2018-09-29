config = {
    'game_url': 'chrome://dino',
    'chrome_driver_path': '/usr/lib/chromium-browser/chromedriver',
    'loss_file_path': './objects/loss_df.csv',
    'actions_file_path': './objects/actions_df.csv',
    'q_values_file_path': './objects/q_values.csv',
    'scores_file_path': './objects/scores_df.csv'
}

canvas = {
    # create id for canvas for faster selection from DOM
    'init_script': 'document.getElementsByClassName("runner-canvas")[0].id = "runner-canvas"',

    # get image from canvas
    'get_base64_script': "canvasRunner = document.getElementById('runner-canvas'); \
return canvasRunner.toDataURL().substring(22)"
}
