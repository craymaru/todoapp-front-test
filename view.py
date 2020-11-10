__pragma__('alias', 'S', '$')


class View:
    def render_todo_list(self, data):
        # ToDoリストを描画する
        S('#todo-list').empty()
        for todo in data:
            S('#todo-list').append(self._create_todo_row(todo))

    def _create_todo_row(self, todo):
        # ToDoの明細行を生成する
        id = todo['id']
        title = todo['title']
        memo = todo['memo']
        priority = ['Low', 'Middle', 'High'][int(todo['priority']) - 1]
        check = 'checked' if todo['completed'] else ''
        return """
            <tr>
                <td>
                    <input type='checkbox' class="toggle-checkbox"
                        id='check-{id}'
                        {check}>
                </td>
                <td>{title}</td>
                <td>{memo}</td>
                <td>{priority}</td>
                <td>
                    <button class='btn btn-outline-primary update-button'
                        id='update-{id}' data-toggle='modal'
                        data-target='#input-form'>Change</button>
                </td>
                <td>
                    <button class='btn btn-outline-danger delete-button'
                        id='delete-{id}'>Delete</button>
                </td>
            </tr>
        """.format(id=id, title=title, memo=memo, priority=priority, check=check)

    def show_new_modal(self):
        # 新規登録のモーダルダイアログを初期化する
        S('#modal-title').text('+ Add')
        S('#modal-todo-id').val('')
        S('#modal-todo-title').val('')
        S('#modal-todo-memo').val('')
        S('#modal-todo-priority').val(1)

    def close_modal(self):
        # モーダルダイアログを閉じる
        S('#input-form').modal('hide')

    def get_input_data(self):
        # モーダルダイアログの入力内容を取得する
        return {
            'id': S('#modal-todo-id').val(),
            'title': S('#modal-todo-title').val(),
            'memo': S('#modal-todo-memo').val(),
            'priority': S('#modal-todo-priority').val(),
        }

    def show_update_modal(self, todo):
        # 変更のモーダルダイアログを表示する
        S('#modal-title').text('Change')
        S('#modal-todo-id').val(todo['id'])
        S('#modal-todo-title').val(todo['title'])
        S('#modal-todo-memo').val(todo['memo'])
        S('#modal-todo-priority').val(todo['priority'])
