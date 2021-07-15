import React, { Component } from 'react';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

export default class ConferenceForm extends Component {

    state = {
        conferenceName: '',
        startDate: '',
        endDate: '',
        subject: '',
        ticketPrice: '',
        nrTickets: ''
    }

    handleInput = e => {
        const formData = {};
        formData[e.target.name] = e.target.value;
        this.setState({ ...formData });
    }

    render() {
        const { onSubmit } = this.props;
        const { conferenceName, startDate, endDate, subject, ticketPrice, nrTickets } = this.state;
        return (
            <Form className="mt-5 d-flex flex-column align-items-center w-50 mx-auto"
                onSubmit={e => {
                    e.preventDefault();
                    onSubmit({
                        variables: {
                            conferenceName,
                            startDate,
                            endDate,
                            subject,
                            ticketPrice,
                            nrTickets
                        }
                    }).then(() => {
                        this.setState({
                            conferenceName: '',
                            startDate: '',
                            endDate: '',
                            subject: '',
                            ticketPrice: '',
                            nrTickets: 's',
                        });
                    }).catch(e => console.log(e));
                }}
            >
                <h2>Create conference</h2>
                <Form.Group controlId="conferenceName" className="w-100">
                    <Form.Label>Conference name:</Form.Label>
                    <Form.Control name="conferenceName" type="text" onChange={this.handleInput} value={conferenceName} />
                </Form.Group>

                <Form.Row className="w-100 d-flex justify-content-between">
                    <Form.Group controlId="startDate" style={{ width: "49%" }}>
                        <Form.Label>Start date:</Form.Label>
                        <Form.Control name="startDate" type="date" onChange={this.handleInput} value={startDate} />
                    </Form.Group>

                    <Form.Group controlId="endDate" style={{ width: "49%" }}>
                        <Form.Label>End date:</Form.Label>
                        <Form.Control name="endDate" type="date" onChange={this.handleInput} value={endDate} />
                    </Form.Group>
                </Form.Row>

                <Form.Group controlId="subject" className="w-100">
                    <Form.Label>Subject:</Form.Label>
                    <Form.Control name="subject" type="text" onChange={this.handleInput} value={subject} />
                </Form.Group>

                <Form.Group controlId="nrTickets" className="w-100">
                    <Form.Label>Tickets number:</Form.Label>
                    <Form.Control name="nrTickets" type="text" onChange={this.handleInput} value={nrTickets} />
                </Form.Group>

                <Form.Group controlId="ticketPrice" className="w-100">
                    <Form.Label>Ticket price:</Form.Label>
                    <Form.Control name="ticketPrice" type="text" onChange={this.handleInput} value={ticketPrice} />
                </Form.Group>

                <Button variant="primary" type="submit" className="button" style={{ fontWeight: "bold" }}>SUBMIT</Button>

            </Form>
        )
    }
}