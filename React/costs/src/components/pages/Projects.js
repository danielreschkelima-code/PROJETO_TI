import { useLocation } from 'react-router-dom';
import { useState, useEffect } from 'react';

import Message from "../layout/Message.js";
import Container from '../layout/Container.js'
import LinkButton from '../layout/LinkButton.js';
import ProjectCard from '../project/ProjectCard.js';

import styles from './Projects.module.css'

function Projects() {

    const [projects, setProjects] = useState([]);

    const location = useLocation();

    let message = '';
    if(location.state) {
        message = location.state.message;
    }

    useEffect(() => {
        fetch('http://localhost:5000/projects', {
            method: 'GET',
            headers: {
                'Content-Type': 'application.json',
            },
        })
        .then((resp) => resp.json())
        .then((data) => {
            console.log(data);
            setProjects(data);
        })
        .catch((err) => console.log(err))
    }, []);

    return (
        <div className={styles.project_container}>
            <div className={styles.title_container}>
                <h1>Meus Projetos</h1>
                <LinkButton to="/newproject" text="Criar Projeto" />
            </div>
            {message && <Message msg={message} type="success" />}
            <Container customCLass="start">
                {projects.length > 0 &&
                    projects.map((project) => (<ProjectCard name={project.name} id={project.id} budget={project.budget} category={project.category ? project.category.name : "Projeto sem categoria"} key={project.id} />
                    ))
                }
            </Container>
        </div>
    );
}

export default Projects;