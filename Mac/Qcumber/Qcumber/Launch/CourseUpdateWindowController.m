//
//  CourseUpdateWindowController.m
//  Qcumber
//
//  Created by Chris Cooper on 11-10-13.
//  Copyright 2011 Chris Cooper. All rights reserved.
//

#import "CourseUpdateWindowController.h"

@implementation CourseUpdateWindowController
@synthesize progressIndicator = progressIndicator_;
@synthesize progressTextField = progressTextField_;

- (id)initWithWindow:(NSWindow *)window
{
    self = [super initWithWindow:window];
    if (self) {
        // Initialization code here.
    }
    
    return self;
}

- (void)windowDidLoad
{
    [super windowDidLoad];
    
    
}

//-(NSString*)windowTitleForDocumentDisplayName:(NSString *)displayName {

@end
