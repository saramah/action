<%inherit file="base.mako"/>
<h1>Todo</h1>    
<span id="arrange">Arrange 
<a href="/task/sort_by_alpha">alphabetically</a>,
<a href="/task/sort_by_deadline">by deadline</a>
</span>

<form method="post" action="/task/complete_task">
    <ul id="todo">
    % for t in c.tasks:
        <li>
            <input type="checkbox" name="${t.id}" />${t}
        </li>
    % endfor
    </ul>
    <input type="submit" value="update tasks" />
</form>


<form method="post" action="/task/add_new">
    <input type="text" name="new_task" />
    <input type="submit" value="Add new task" />
</form>

<a href="#">see completed tasks</a>

<ul id="done">
% for d in c.done_tasks:
    <li>${d}</li>
% endfor
</ul>
