import React, { Component } from 'react'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

export default class PaperForm extends Component {
    state = {
        abstract: false,
        paperContent: '',
        title: '',
    }

    handleInput = e => {

        const formData = {};
        formData[e.target.name] = e.target.value;
        this.setState({ ...formData });
    }

    handleChangeCheckbox = e => {
        console.log(this.state.abstract);
        this.state.abstract = !this.state.abstract;
    }

    render() {
        // console.log("prop=" + this.props.id);
        const { onSubmit } = this.props;
        const { abstract, paperContent, title } = this.state;
        return (
            <Form className="mt-5 d-flex flex-column align-items-center w-50 mx-auto"
                onSubmit={e => {
                    e.preventDefault();
                    onSubmit({
                        variables: {
                            conferenceId: this.props.id,
                            abstract: this.state.abstract,
                            paperContent,
                            title
                        }
                    }).then(() => {
                        this.setState({
                            conferenceId: this.props.id,
                            abstract: !this.state.abstract,
                            paperContent: '',
                            title: ''
                        });
                    }).catch(e => console.log(e));
                }}
            >
                <h2>Add paper</h2>

                <Form.Group controlId="titleInput" className="w-100 mt-3">
                    <Form.Label>Paper title: </Form.Label>
                    <Form.Control name="title" type="text" onChange={this.handleInput} value={title}  />
                </Form.Group>

                <Form.Group controlId="nrTipaperContentckets" className="w-100 mt-3">
                    <Form.Label>Paper content: </Form.Label>
                    <Form.Control name="paperContent" as="textarea" onChange={this.handleInput} value={paperContent} style={{ height: '300px' }} />
                </Form.Group>

                <Form.Group controlId="abstract" className="w-100">
                    <Form.Check name="abstract" label="abstract (by checking this you agree to upload the full paper later)" type="checkbox" onChange={this.handleChangeCheckbox} defaultChecked={abstract} value={this.state.abstract} style={{ width: '100', height: '36' }} />
                </Form.Group>

                <Button type="submit" className="button" style={{}}>SUBMIT</Button>

            </Form>
        )
    }
}
