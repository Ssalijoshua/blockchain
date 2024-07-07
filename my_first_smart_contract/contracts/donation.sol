// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Donation {
    address public donatur;
    address payable donatee;
    uint public money;
    string public useless_variable;

    constructor() {
        donatee = payable(msg.sender);
        useless_variable = "Donation string";
    }

    function change_useless_variable(string memory param) public {
        useless_variable = param;
    }

    function donate() public payable {
        require(msg.value > 0, "Donation must be greater than 0");
        donatur = msg.sender;
        money = msg.value;
    }

    function receive_donation() public {
        require(msg.sender == donatee, "Only the donatee can receive donations");
        donatee.transfer(address(this).balance);
    }

    receive() external payable {
        donate();
    }
}
