import React from "react";
import {
  Col,
  Row,
  Jumbotron,
  Form,
  Button,
  Container,
} from "react-bootstrap";
import DogForm from "./DogForm";
import CatForm from "./CatForm";

class PetApp extends React.Component {
  constructor(props) {
    super(props);

    this.state = { isDogPage: false, isCatPage: false, isClientPage: true };

    this.enableDogPage = this.enableDogPage.bind(this);
    this.enableCatPage = this.enableCatPage.bind(this);
  }
  enableDogPage() {
    this.setState({ isDogPage: true, isCatPage: false, isClientPage: false });
  }
  enableCatPage() {
    this.setState({ isDogPage: false, isCatPage: true, isClientPage: false });
  }

  render() {
    let clientComp = (
      <Container>
        <Row>
          <Col md={{ span: 7, offset: 3 }}>
            <Jumbotron>
              <h1>New Client Patient Form</h1>
              <p>
                Are you or your pet new to React? Please fill out this simple
                form with as much of your information as you can provide , and
                it will be sent directly to us in preparation for your first
                appointment.
              </p>
              <Form>
                <Form.Group>
                  <h2>Owner Information</h2>
                  <Form.Label>Name</Form.Label>
                  <Form.Row>
                    <Col>
                      <Form.Control placeholder="First name"></Form.Control>
                    </Col>
                    <Col>
                      <Form.Control placeholder="Last name"></Form.Control>
                    </Col>
                  </Form.Row>
                </Form.Group>
                <Form.Row>
                  <Form.Group as={Col} controlId="formGridEmail">
                    <Form.Label>Email</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" />
                  </Form.Group>
                  <Form.Group as={Col} controlId="formGridTel">
                    <Form.Label>Telephone</Form.Label>
                    <Form.Control type="telephone" placeholder="Enter phone" />
                  </Form.Group>
                </Form.Row>
                <Form.Group controlId="formGridAddress1"></Form.Group>
                <Form.Label>Address</Form.Label>
                <Form.Control placeholder="Street name" />
                <Form.Group controlId="formGridAddress2">
                  <Form.Label>Address 2</Form.Label>
                  <Form.Control placeholder="Unit, apartment, etc." />
                </Form.Group>
                <Form.Row>
                  <Form.Group as={Col} controlId="formGridCity">
                    <Form.Label>City</Form.Label>
                    <Form.Control />
                  </Form.Group>
                  <Form.Group as={Col} controlId="formGridState">
                    <Form.Label>State</Form.Label>
                    <Form.Control as="select">
                      <option>Choose...</option>
                      <option>...</option>
                    </Form.Control>
                  </Form.Group>
                  <Form.Group as={Col} controlId="formGridZip">
                    <Form.Label>Zip</Form.Label>
                    <Form.Control />
                  </Form.Group>
                </Form.Row>
                <h2>Pet Type</h2>
                <Container>
                  <Row>
                    <Col>
                      <Button
                        variant="primary"
                        type="submit"
                        size="lg"
                        onClick={this.enableDogPage}
                      >
                        Dog
                      </Button>
                    </Col>
                    <Col>
                      <Button
                        variant="primary"
                        type="submit"
                        size="lg"
                        onClick={this.enableCatPage}
                      >
                        Cat
                      </Button>
                    </Col>
                  </Row>
                </Container>
              </Form>
            </Jumbotron>
          </Col>
        </Row>
      </Container>
    );

    return (
      <div>
        {this.state.isClientPage ? clientComp : null}
        {this.state.isDogPage ? <DogForm/> : null}
        {this.state.isCatPage ? <CatForm/> : null}
      </div>
    );
  }
}

export default PetApp;
