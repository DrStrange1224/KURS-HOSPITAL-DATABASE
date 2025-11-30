<h1>Client for hospital database.</h1>

<code>uitf.py</code> - script turns <code>.ui</code> files in <b><i>.\\uis\\</i></b> folder to <code>.py</code> files in <b><i>.\\py_uis\\</i></b> folder

<b>IMPORTANT THINGS</b>:
1. <code>pyqt_ver</code> branch created on python version of 3.9.13

2. REQUIRED FILES:
<ul>
<li><b><i>config.ini</i></b> - it includes some settings of your postgresql server:<br/>

<code>[postgresql]<br/>
<b>host</b> = &lt;your_server_host_name&gt;<br/>
<b>port</b> = &lt;your_server_port&gt;<br/>
<b>dbname</b> = &lt;your_database_name&gt;<br/>
<b>user</b> = &lt;your_user_name&gt;<br/>
<b>password</b> = &lt;your_password&gt;<br/></code></li>
</ul>

3. Install packages from <code>requirements.txt</code>: <code>pip install -r /path/to/requirements.txt</code>