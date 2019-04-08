pragma solidity ^0.4.24;

contract RefundablePurchase {

    event Refund(address, uint256);
    event PurchaseCompleted(address, uint256);

    address owner;

    mapping (address => uint256) public refunds;

    constructor() public payable {
        require(msg.value == 0.5 ether, "Must send 0.5 Ether");
    }

    /** Fallback function, called when contract receives Ether without data
     */
    function () external payable {
        require(refunds[msg.sender] + msg.value > refunds[msg.sender]); // Overflow guard
        refunds[msg.sender] += msg.value;
    }

    /** Refunds sent Ether
     */
    function refund() public {
        require(refunds[msg.sender] > 0);
        uint256 amount = refunds[msg.sender];
        msg.sender.call.value(amount)("");
        refunds[msg.sender] = 0;
        emit Refund(msg.sender, amount);
    }

    /** Call this function once you've received your purchased item
     */
    function completePurchase() public {
        require(refunds[msg.sender] > 0);
        uint256 amount = refunds[msg.sender];
        refunds[msg.sender] = 0;
        emit PurchaseCompleted(msg.sender, amount);
    }

    /** Returns balance of this contract
     */
    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }

    /** CTF helper function
     *  Used to check if challenge is complete
     */
    function isComplete() public view returns (bool) {
        return address(this).balance == 0;
    }

}