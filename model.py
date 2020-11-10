from const import BASE_URL
__pragma__('alias', 'S', '$')


class Model:
    def __init__(self):
        self._todos = []

    def get_todo(self, todo_id):
        # 指定されたIDのToDoを取得する
        for todo in self._todos:
            if todo['id'] == todo_id:
                return todo
        return None

    def get_all_todos(self):
        # すべてのToDoを取得する
        return self._todos

    def load_all_todos(self):
        # 全件取得のAPIを呼び出す
        S.ajax({
            'url': BASE_URL + "todos",
            # 'url': 'http://127.0.0.1:8000/todos',
            'type': 'GET',
        }).done(
            self._success_load_all_todos
        ).fail(
            lambda d: alert('サーバーとの通信に失敗しました。')
        )

    def _success_load_all_todos(self, data):
        # load_all_todos()成功時の処理
        self._todos = data
        S('body').trigger('todos-updated')

    def create_todo(self, data):
        # ToDo登録のAPIを呼び出す
        S.ajax({
            'url': BASE_URL + "todos",
            'type': 'POST',
            'contentType': 'application/json',
            'data': JSON.stringify(data),
        }).done(
            self._success_create_todo
        ).fail(
            lambda d: alert('サーバーとの通信に失敗しました。')
        )

    def _success_create_todo(self, data):
        # create_todo()成功時の処理
        self._todos.append(data)
        S('body').trigger('todos-updated')

    def update_todo(self, todo_id, data):
        # ToDo更新のAPIを呼び出す
        send_data = {}
        for key in ['title', 'memo', 'priority', 'completed']:
            if key in data:
                send_data[key] = data[key]
        S.ajax({
            'url': BASE_URL+"todos/"+todo_id,
            'type': 'PUT',
            'contentType': 'application/json',
            'data': JSON.stringify(send_data),
        }).done(
            self._success_update_todo
        ).fail(
            lambda d: alert('サーバーとの通信に失敗しました。')
        )

    def _success_update_todo(self, data):
        # update_todo()成功時の処理
        for i, todo in enumerate(self._todos):
            if todo['id'] == data['id']:
                self._todos[i] = data
        S('body').trigger('todos-updated')

    def toggle_todo(self, todo_id):
        # 完了状態を反転する
        todo = self.get_todo(todo_id)
        self.update_todo(todo_id, {'completed': not todo['completed']})

    def delete_todo(self, todo_id):
        # ToDo削除のAPIを呼び出す
        S.ajax({
            'url': BASE_URL+"todos/"+todo_id,
            'type': 'DELETE',
        }).done(
            self._success_delete_todo
        ).fail(
            lambda d: alert('サーバーとの通信に失敗しました。')
        )
    def _success_delete_todo(self, data):
        # delete_todo()成功時の処理
        for i, todo in enumerate(self._todos):
            if todo['id'] == data['id']:
                self._todos.pop(i)
                break
        S('body').trigger('todos-updated')