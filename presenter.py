__pragma__('alias', 'S', '$')
from model import Model
from view import View


class Presenter:
    def __init__(self):
        self._model = Model()
        self._view = View()
        self._bind()

    def _bind(self):
        # イベントをバインドする
        S('body').on('todos-updated', self._on_todos_updated) # ToDoリスト更新
        S('#input-form').on('show.bs.modal', self._on_show_modal) # Modal表示時
        S('#register-button').on('click', self._on_click_register) # 新規ToDo登録時
        S('#todo-list').on('click', '.toggle-checkbox', self._on_click_checkbox) # チェックボックストグル時
        S('#todo-list').on('click', '.delete-button', self._on_click_delete) # 削除時

    def start(self):
        # 初期表示処理
        self._model.load_all_todos()

    def _on_todos_updated(self, event):
        # todos-updated受信時の処理
        self._view.render_todo_list(self._model.get_all_todos())

    def _on_show_modal(self, event):
        # show.bs.modal受信時の処理
        target_id = S(event.relatedTarget).attr('id')
        if target_id == 'new-todo':
            self._view.show_new_modal()
        elif target_id.startswith('update-'):
            todo_id = target_id[7:]
            todo = self._model.get_todo(todo_id)
            self._view.show_update_modal(todo)


    def _on_click_register(self, event):
        # register-buttonのclick受信時の処理
        input_data = self._view.get_input_data()
        if input_data['id']:
            self._model.update_todo(input_data['id'], input_data)
        else:
            self._model.create_todo(input_data)
        self._view.close_modal()

    def _on_click_checkbox(self, event):
        # toggle-checkboxのclick受信時の処理
        target_id = S(event.target).attr('id')
        if target_id.startswith('check-'):
            todo_id = target_id[6:]
            self._model.toggle_todo(todo_id)

    def _on_click_delete(self, event):
        # delete-buttonのclick受信時の処理
        target_id = S(event.target).attr('id')
        if target_id.startswith('delete-'):
            todo_id = target_id[7:]
            self._model.delete_todo(todo_id)