import flet as ft

def main(page: ft.Page):

    
    def add_task(e):
        if task_input.value != "":
            task_list.controls.append(ft.Text(task_input.value))
            task_input.value = ""
            page.update()

    task_input = ft.TextField(hint_text="Digite o nome da tarefa", expand=True)

    add_button = ft.ElevatedButton(text="Adicionar", on_click=add_task)


    task_list = ft.Column()

    
    page.add(
        ft.Row([task_input, add_button], alignment="center"),
        task_list
    )

ft.app(target=main)