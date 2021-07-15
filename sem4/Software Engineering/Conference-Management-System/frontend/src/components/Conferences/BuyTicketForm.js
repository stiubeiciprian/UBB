import React, { Component } from 'react';

export default class BuyTicketForm extends Component {

    state = {
        conferenceName: '',
        startDate: '',
        endDate: '',
        subject: '',
        nrTickets: '100'
    }

    handleInput = e => {
        const formData = {};
        formData[e.target.name] = e.target.value;
        this.setState({ ...formData });
    }

    render() {
        const { onSubmit } = this.props;
        const { conferenceName, startDate, endDate, subject, nrTickets } = this.state;
        return (
            <form
                onSubmit={e => {
                    e.preventDefault();
                    onSubmit({
                        variables: {
                            conferenceName,
                            startDate,
                            endDate,
                            subject,
                            nrTickets
                        }
                    }).then(() => {
                        this.setState({
                            conferenceName: '',
                            startDate: '',
                            endDate: '',
                            subject: '',
                            nrTickets: 's',
                        });
                    }).catch(e => console.log(e));
                }}
            >
                <div class="form-group card">
                    <h2 class="title-register">Create new conference</h2>
                    <label for="cname">Conference name:</label>
                    <input type="text" name="conferenceName" onChange={this.handleInput} value={conferenceName} id="cname" className="form-control form-control-lg rounded-0" /><br />

                    <label for="sdate">Start date:</label>
                    <input type="date" name="startDate" onChange={this.handleInput} value={startDate} id="sdate" className="form-control form-control-lg rounded-0" /><br />

                    <label for="edate">End date:</label>
                    <input type="date" name="endDate" onChange={this.handleInput} value={endDate} id="edate" className="form-control form-control-lg rounded-0" /><br />

                    <label for="sbj">Subject:</label>
                    <input type="text" name="subject" onChange={this.handleInput} value={subject} id="sbj" className="form-control form-control-lg rounded-0" /><br />

                    <label for="nrtickets">Nr. tickets:</label>
                    <input type="text" disabled={true} name="tickets" onChange={this.handleInput} value={nrTickets} id="nrtickets" className="form-control form-control-lg rounded-0" /><br />

                    <input type="submit" value="Submit" class="btn btn-dark" />
                </div>
            </form>
        )
    }
}