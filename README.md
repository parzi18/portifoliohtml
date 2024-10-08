# portifolio
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Portfólio</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e9ecef;
            color: #333;
        }
        header {
            background: #007bff;
            color: white;
            padding: 20px 0;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        nav {
            margin: 20px 0;
        }
        nav a {
            margin: 0 15px;
            color: #f4f4f4;
            text-decoration: none;
            transition: color 0.3s;
            font-weight: 500;
        }
        nav a:hover {
            color: #d1d1d1;
            border-bottom: 2px solid #f4f4f4;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
            padding: 20px 0;
        }
        .about, .projects, .contact {
            background: white;
            margin: 20px 0;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }
        .about:hover, .projects:hover, .contact:hover {
            transform: translateY(-5px);
        }
        .project {
            margin: 15px 0;
            padding: 15px;
            border-left: 4px solid #007bff;
            background-color: #f9f9f9;
            border-radius: 5px;
        }
        .project h3 {
            margin-top: 0;
            color: #007bff;
        }
        footer {
            text-align: center;
            padding: 15px 0;
            background: #007bff;
            color: white;
            position: relative;
            bottom: 0;
            width: 100%;
            margin-top: 20px;
        }
        /* Estilo do botão */
        .button {
            display: inline-block;
            padding: 10px 20px;
            background: #28a745;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            transition: background 0.3s;
        }
        .button:hover {
            background: #218838;
        }
        /* Responsividade */
        @media (max-width: 768px) {
            .container {
                width: 95%;
            }
            nav a {
                display: block;
                margin: 10px 0;
            }
        }
    </style>
</head>
<body>

<header>
    <h1>Meu Portfólio</h1>
    <nav>
        <a href="#about">Sobre Mim</a>
        <a href="#projects">Projetos</a>
        <a href="#contact">Contato</a>
    </nav>
</header>

<div class="container">
    <section id="about" class="about">
        <h2>Sobre Mim</h2>
        <p>Olá! Sou Pedro Moreno, um estudante de programação apaixonado por desenvolvimento de jogos. Aqui estão alguns dos meus projetos.</p>
    </section>

    <section id="projects" class="projects">
        <h2>Projetos</h2>
        <div class="project">
            <h3>Projeto 1: Bot em Python</h3>
            <p>Um bot feito para abrir seu WhatsApp Web e ler suas mensagens não lidas. <a class="button" href="#">Ver mais</a></p>
        </div>
    </section>

    <section id="contact" class="contact">
        <h2>Contato</h2>
        <p>Você pode me encontrar em:</p>
        <ul>
            <li>Email: <a href="mailto:pedromv2006@gmail.com">pedromv2006@gmail.com</a></li>
            <li>GitHub: <a href="https://github.com/Pari_18" target="_blank">Pari_18</a></li>
        </ul>
    </section>
</div>

<footer>
    <p>&copy; 2024 Meu Portfólio. Todos os direitos reservados.</p>
</footer>

</body>
</html>
